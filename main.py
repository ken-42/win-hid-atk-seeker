import argparse
import sys
import datetime
from exec1_1 import extractUSB
from exec2 import shimcache_analysis
from prefetch_extractor import prefetch_extractor
from all_events_parser import events_parser
from Usb import Usb 
from util import write_it, thanks

def main(): #in input va specificato l'hive SYSTEM
    parser = argparse.ArgumentParser(description="Hive SYSTEM for the extraction of USBs")
    parser.add_argument("hiveSys", type=str, help="Path to the hive SYSTEM")
    args = parser.parse_args()
    print("USB extraction in progress...")
    try:
        usb_list = extractUSB(sys.argv[1]) #estrazione di tutte le subkey di USB
        print("[+] Extraction successful!\n\n")
        while True:
            print("What do you do?\n")
            print("1 - Give me information about all USB keys\n")
            print("2 - Go to temporal analysis\n")
            print("0 - Exit\n")
            r1 = input("Press 1, 2 or 0: ")
            if(r1 == "1"):
                usb_output = ""
                for usb in usb_list:
                    usb_string = usb.toString()
                    print(usb_string)
                    usb_output += usb_string
                write_it(usb_output, "usb_list.txt")
            elif(r1 == "2"):
                print("\nSelect an ID to continue:\n")
                for usb in usb_list:
                    print("ID: " + str(usb.getKeyID()) + " - VID_" + usb.getVendorID() + "&PID_" + usb.getProductID() + " - Serial Number: " + usb.getSerialNumber()[0] + "\n")
                keyId = int(input("Enter an ID: "))
                if(keyId >= 0 and keyId <= len(usb_list)-1):
                    usb_selected = usb_list[keyId]
                    start_date = usb_selected.getDeviceFirstInstallDate()[0]
                    end_date = usb_selected.getDeviceLastRemovalDate()[-1]
                    print("\nThe temporal analysis will be performed between " + str(start_date) + " and " + str(end_date) + ".\n")
                    while True:
                        print("Select what you want to analyze:\n")
                        print("0 - Go back\n")
                        print("1 - Shimcache Hive\n")
                        print("2 - Prefetch Files\n")
                        print("3 - Windows Events\n")
                        r2 = input("Press 0, 1, 2 or 3: ")
                        if(r2 == "0"):
                            break
                        elif(r2 == "1"):
                            shimcache_analysis(sys.argv[1], start_date, end_date)
                        elif(r2 == "2"):
                            prefetch_path = input("Insert Prefetch directory path (usually C:\\Windows\\Prefetch): ")
                            prefetch_extractor(prefetch_path, start_date, end_date)
                        elif(r2 == "3"):
                            events_path = input("Insert Windows Events directory path (usually C:\\Windows\\System32\\winevt\\Logs): ")
                            events_parser(events_path, start_date, end_date)
                        else:
                            print("\n\n*facepalm*\n\n")
                else:
                    print("USB not exists...")
            elif(r1 == "0"):
                print("[-] EXIT...")
                sys.exit()
            else:
                print("I don't believe it... BYE!")
                sys.exit(1)
    except:
        print("[-] EXIT...")
        thanks()
        sys.exit(1)

if __name__ == "__main__":
    main()