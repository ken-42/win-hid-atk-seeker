import pyscca
import os
from util import write_it

def prefetch_extractor(prefetch_path, start_date, end_date):
    output = ""
    for _, _, files in os.walk(prefetch_path):
        for file in files:
            if file.endswith(".pf"):
                pfFile = pyscca.file()
                pfFile.open(prefetch_path + "/" + file)
                if(pfFile.get_last_run_time(0) >= start_date and pfFile.get_last_run_time(0) <= end_date):
                    output += "===================\n"
                    output += str(pfFile.executable_filename) + "-" + hex(pfFile.prefetch_hash).lstrip("0x").rstrip("L").upper() + ".pf\n"
                    output += "===================\n"
                    output += "\nExecutable Name: " + str(pfFile.executable_filename) + "\n\n"
                    output += "Run count: " + str(pfFile.run_count) + "\n\n"
                    output += "Last executed: " + str(pfFile.get_last_run_time(0)) + "\n"
                    if pfFile.format_version >= 26:
                        for i in range(2,8):
                            if str(pfFile.get_last_run_time(i))[0:4] != "1601":
                                output += "               " + str(pfFile.get_last_run_time(i)) + "\n"
                    output += "\nVolumes Information:"
                    for i in pfFile.volumes:
                        output += "\n        Name: " + str(i.device_path)[1:]
                        output += "\n        Creation Date: " + str(i.creation_time)
                        output += "\n        Serial Number: " + hex(i.serial_number).lstrip("0x").rstrip("L")
                        output += "\n"
                    output += "\nResources Loaded:\n"
                    cont = 0
                    for i in pfFile.filenames:
                        cont += 1
                        output += str(cont) + ": " + i + "\n"
                    output += "\n\n\n"
                pfFile.close()
    write_it(output, "prefetch_output.txt")