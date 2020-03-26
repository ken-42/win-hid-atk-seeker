import sys
import struct
import datetime
from io import BytesIO
from os import path
from Registry import Registry

# Values used by Windows 10
WIN10_STATS_SIZE = 0x30
WIN10_CREATORS_STATS_SIZE = 0x34
WIN10_MAGIC = '10ts'

bad_entry_data = 'N/A'
output_header  = ["Last Modified", "Last Update", "Path", "File Size", "Exec Flag"]

# Date Formats
DATE_MDY = "%m/%d/%y %H:%M:%S"
DATE_ISO = "%Y-%m-%d %H:%M:%S"
g_timeformat = DATE_ISO


def convert_filetime(dwLowDateTime, dwHighDateTime):

    try:
        date = datetime.datetime(1601, 1, 1, 0, 0, 0)
        temp_time = dwHighDateTime
        temp_time <<= 32
        temp_time |= dwLowDateTime
        return date + datetime.timedelta(microseconds=temp_time/10)
    except OverflowError:
        return None

# Read the Shim Cache format, return a list of last modified dates/paths.
def read_cache(cachebin, start_date, end_date, quiet=False):
    
    if len(cachebin) < 16:
        # Data size less than minimum header size.
        return None
    
    try:
        # Get the format type
        magic = struct.unpack("<L", cachebin[0:4])[0]
        # Windows 10 will use a different magic dword, check for it
        if len(cachebin) > WIN10_STATS_SIZE and cachebin[WIN10_STATS_SIZE:WIN10_STATS_SIZE+4].decode("utf-8") == WIN10_MAGIC:
            if not quiet:
                print("[+] Found Windows 10 Apphelp Cache data...")
            return read_win10_entries(cachebin, WIN10_MAGIC, start_date, end_date)
        
        # Windows 10 Creators Update will use a different STATS_SIZE, account for it
        elif len(cachebin) > WIN10_CREATORS_STATS_SIZE and cachebin[WIN10_CREATORS_STATS_SIZE:WIN10_CREATORS_STATS_SIZE+4].decode("utf-8") == WIN10_MAGIC:
            if not quiet:
                print("[+] Found Windows 10 Creators Update Apphelp Cache data...")
            return read_win10_entries(cachebin, WIN10_MAGIC, start_date, end_date, creators_update=True)
        
        else:
            print("[-] Got an unrecognized magic value of 0x", magic, "... bailing")
            return None
    
    except (RuntimeError, TypeError, NameError) as err:
        print("[-] Error reading Shim Cache data: ", err)
        return None

# Read Windows 10 Apphelp Cache entry format
def read_win10_entries(bin_data, ver_magic, start_date, end_date, creators_update=False):
    
    entry_meta_len = 12
    entry_list = []

    # Skip past the stats in the header
    if creators_update:
        cache_data = bin_data[WIN10_CREATORS_STATS_SIZE:]
    else:
        cache_data = bin_data[WIN10_STATS_SIZE:]

    data = BytesIO(cache_data)
    while data.tell() < len(cache_data):
        header = data.read(entry_meta_len)
        # Read in the entry metadata
        # Note: the crc32 hash is of the cache entry data
        magic, crc32_hash, entry_len = struct.unpack('<4sLL', header)

        # Check the magic tag
        if magic.decode("ascii") != ver_magic:
            raise Exception("Invalid version magic tag found: ", struct.unpack("<L", magic)[0])

        entry_data = BytesIO(data.read(entry_len))

        # Read the path length
        path_len = struct.unpack('<H', entry_data.read(2))[0]
        if path_len == 0:
            path = 'None'
        else:
            path8 = entry_data.read(path_len).decode('utf-16le', 'replace').encode('utf-8')
            path = path8.decode("utf-8")

        # Read the remaining entry data
        low_datetime, high_datetime = struct.unpack('<LL', entry_data.read(8))

        last_mod_date = convert_filetime(low_datetime, high_datetime)
        if(last_mod_date >= start_date and last_mod_date <= end_date):
            try:
                last_mod_date = last_mod_date.strftime(g_timeformat)
            except ValueError:
                last_mod_date = bad_entry_data
    
            # Skip the unrecognized Microsoft App entry format for now
            if last_mod_date == bad_entry_data:
                continue

            row = [last_mod_date, 'N/A', path, 'N/A', 'N/A']
            entry_list.append(row)

    return entry_list


def read_from_hive(hive, start_date, end_date):
    out_list = []
    tmp_list = []

    try:
        reg = Registry.Registry(hive)
    except Registry.RegistryParse.ParseException as err:
        print("[-] Error parsing ", hive, ": ", err)
        sys.exit(1)

    try:
        appCompatCachePath = r"ControlSet001\Control\Session Manager\AppCompatCache"
        appCompatCacheKey = reg.open(appCompatCachePath)
        appCompatCacheValue = appCompatCacheKey['AppCompatCache']
        dataOfAppCompatCacheValue = appCompatCacheValue.value()
        tmp_list = read_cache(dataOfAppCompatCacheValue, start_date, end_date)
        if tmp_list:
            for row in tmp_list:
                if row not in out_list:
                    out_list.append(row)
    except Registry.RegistryKeyNotFoundException:
        print("[-] Key not found")
    except Registry.RegistryValueNotFoundException:
        print("[-] Value not found")

    if len(out_list) == 0:
        return None
    else:
        # Add the header and return the list including duplicates.
        out_list.insert(0, output_header)
        return out_list