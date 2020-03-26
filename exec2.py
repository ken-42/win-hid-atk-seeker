from support_2 import read_from_hive
from util import write_it

def shimcache_analysis(systemHive, start, end):
    print("[+] Reading registry hive: SYSTEM...")
    try:
        entries = read_from_hive(systemHive, start, end)
        if not entries:
            print("[-] No Shim Cache entries found...")
        else:
            write_it(entries, "shimcache_output.csv", "csv")
    except IOError as err:
        print("[-] Error opening hive file: ", str(err))
