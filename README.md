# Windows HID Attack Seeker

Windows HID Attack Seeker is a Phyton3 tool that allows you to study some digital evidence to help detect HID attacks on Windows 10.

This tool has been tested with Tsurugi Linux.


![alt text](https://github.com/ken-42/win-hid-atk-seeker/blob/master/images/logo.png)



### Requirements:
- python3
- python-registry: https://github.com/williballenthin/python-registry
- libscca: https://github.com/libyal/libscca
- python-evtx: https://github.com/williballenthin/python-evtx



## Usage:
The analysis can be started by running the command:
```
python3 main.py SYSTEM
```
where SYSTEM indicates the Windows 10 SYSTEM hive.

To continue the analysis you need:
- prefetch files: C:\Windows\Prefetch
- event log files: C:\Windows\System32\winevt\Logs

To extract data from ShimCache a part of the https://github.com/mandiant/ShimCacheParser code has been converted to python3
