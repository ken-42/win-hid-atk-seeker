from csv import writer
from xml.etree import ElementTree
import datetime

def write_it(rows, outfile=None, type="txt"):
    try:
        if not rows:
            print("[-] No data to write...")
            return
        print("[+] Writing output to", outfile, "...")
        try:
            f = open(outfile, 'w')
            if(type == "txt"):
                f.write(rows)
            else:
                csv_writer = writer(f, delimiter=',')
                csv_writer.writerows(rows)
            f.close()
            print("[+] Output file was created in current directory!\n")
        except IOError as err:
            print("[-] Error writing output file: ", str(err))
            return
    except UnicodeEncodeError as err:
        print("[-] Error writing output file: ", str(err))
        return

def xml_to_txt(fileXML):
    tree = ElementTree.parse(fileXML)
    root0 = tree.getroot()
    output = ""
    for root in root0: #root0 = <Logs>; root = <Events evtxName=...>
        for attr in root.attrib:
            output += "=============================================\n"
            output += "Events from log: " + root.attrib[attr] + "\n"
            output += "=============================================\n"
        for child in root: #child = <Event xmlns="...">
            output += "===================================\n"
            output += child.tag.split("}")[1]
            if str(child.attrib) == "{}":
                output += "\n"
            else:
                output += str(child.attrib) + "\n"
            for child2 in child: #child2 = System oppure EventData
                output += "\t" + child2.tag.split("}")[1] + ":\n"
                for child3 in child2: #child3 = Provider oppure EventIP ecc
                    output += "\t\t" + child3.tag.split("}")[1] + ":"
                    if child3.text:
                        output += " " + child3.text
                    output += "\n"
                    if child3.attrib:
                        for attr in child3.attrib:
                            output += "\t\t\t" + attr + ": " + child3.attrib[attr] + "\n" 
                    for child4 in child3:
                        output += "\t\t\t\t" + child4.tag.split("}")[1] + ":"
                        if child4.text:
                            output += " " + child4.text
                        output += "\n"
                        if child4.attrib:
                            for attr in child4.attrib:
                                output += "\t\t\t\t\t" + attr + ": " + child4.attrib[attr] + "\n"
            output += "===================================\n\n\n\n\n"
    write_it(output, "events.txt")

def dateFromLittleEndian(hexLittleDate):
    interval = int.from_bytes(hexLittleDate, 'little', signed=False)
    day0 = datetime.datetime(1601, 1, 1)
    delta = datetime.timedelta(microseconds = interval/10)
    dayN = day0 + delta
    return dayN

def thanks():
	print("Implemented by Giuseppe Pratticò \n")
	print("Revised by Matteo Redaelli \n\n")
	print("Special Thanks to:\nIrene Causo\nPaola Meroni\nStefania Pazienza\nAndrea Di Florio\nDaniele Monico\nFilippo Volpi\nMarco Aveta\nMarco Gontel\nVittorio Addeo\n")
	print("At last but not least, Special Thanks to Andrea Scordino\n\n")
