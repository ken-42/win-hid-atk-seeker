# Windows HID Attack Seeker :detective:

Windows HID Attack Seeker is a Phyton3 tool that allows you to extract information from some digital evidence to help detect HID attacks on Windows 10.

| Evidences | Supported |
| --- | --- |
| USB Devices information | :heavy_check_mark: |
| ShimCache/AppCompatCache | :heavy_check_mark: |
| Prefetch | :heavy_check_mark: |
| Windows Logs | :heavy_check_mark: |
| MRU List | :x: |
| AmCache | :x: |

This tool has been tested on Tsurugi Linux.


![alt text](https://github.com/ken-42/win-hid-atk-seeker/blob/master/images/logo.png)


### Requirements :package:
- python3
- python-registry: https://github.com/williballenthin/python-registry
- libscca: https://github.com/libyal/libscca
- python-evtx: https://github.com/williballenthin/python-evtx

### Notes :memo:
To extract data from ShimCache a part of the https://github.com/mandiant/ShimCacheParser code has been converted to Python3.

## Usage :electric_plug:
Run the tool with the command:
```
python3 main.py SYSTEM
```
where ```SYSTEM``` is the Windows 10 SYSTEM hive.

### First step: USB Information gathering - Which USB and When :computer:
The tool detect USB devices detected from OS that you analyze.

At this point you can:
- press ```1``` to print all information gathered regarding all USB detected, identified with a ```dummy ID``` or
- press ```2``` to go to the next step.


### Second step: Temporal interval definition :clock3:
The collection of information regarding this step is done based on the timestamps of insert and eject that every USB detected have.
When you press ```2``` on previous step, you can choose a USB device (typing a ```dummy ID```) to set temporal interval used to define which information extract from Prefetch and Logs files.


### Third step: ShimCache, Prefetch and Logs Informatin gathering - Input & Output :shipit:
Once the interval is set, you can choose what information extract on an output file:
- press ```1``` for ShimCache (information extracted from SYSTEM hive, already in input);
- press ```2``` for Prefetch;
- press ```3``` for Windows Log.

In cases ```2``` and ```3``` you must set the directory of the files that you choose.
On Windows 10 these directory are respectively in *C:\Windows\Prefetch* and *C:\Windows\System32\winevt\Logs*.

Outputs are provided in .csv for ShimCache, .txt for Prefetch and .xml and .txt for Logs.
