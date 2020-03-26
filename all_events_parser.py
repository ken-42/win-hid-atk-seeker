import Evtx.Evtx as evtx
import Evtx.Views as e_views
import os
from util import write_it, xml_to_txt

def events_parser(pathLogs, start_date, end_date):
    output = e_views.XML_HEADER + "\n"
    output += "\n<Logs>\n"
    for _, _, files in os.walk(pathLogs):
        for file in files:
            if file.endswith(".evtx"):
                with evtx.Evtx(pathLogs + "/" + file) as log:
                    output += "\n" + '<Events evtxName="' + file + '">'
                    for record in log.records():
                        if(record.timestamp() >= start_date and record.timestamp() <= end_date):
                            try:
                                output += "\n\n\n" + record.xml()
                            except:
                                print("Key error")
                    output += "\n" + "</Events>"
                output += "\n\n\n\n\n\n\n\n"
    output += "</Logs>"
    write_it(output, "all-events.xml")
    xml_to_txt("all-events.xml")
