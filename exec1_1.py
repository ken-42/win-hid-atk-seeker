from Registry import Registry
from Usb import Usb
from util import dateFromLittleEndian

def extractUSB(hiveSystem):
    reg = Registry.Registry(hiveSystem)
    usbPath = r"ControlSet001\Enum\USB"
    try:
        usbKey = reg.open(usbPath)
    except Registry.RegistryKeyNotFoundException:
        print("Couldn't find USB key. Exiting...")
    
    usbFinalList = []
    
    for i in usbKey.subkeys():
        try:
            vIDpIDKey = i
            if vIDpIDKey.name()[0:8] != "ROOT_HUB":
                device = Usb(len(usbFinalList))
                device.setVendorID(vIDpIDKey.name()[4:8])
                device.setProductID(vIDpIDKey.name()[13:17])
                for j in vIDpIDKey.subkeys():
                    try:
                        serialNumberKey = j
                        classSubclassProtocol = serialNumberKey.value("CompatibleIDs").value()
                        classSubclassProtocolSplit = classSubclassProtocol[0].split("_")
                        descriptionSplit = serialNumberKey.value("DeviceDesc").value().split(";")
                        deviceMfgSplit = serialNumberKey.value("Mfg").value().split(";")
                        device.getSerialNumber().append(serialNumberKey.name())
                        device.getDescription().append(descriptionSplit[1])
                        if(len(classSubclassProtocolSplit) >= 3):
                            device.getUsbClass().append(classSubclassProtocolSplit[1][0:2])
                            device.getUsbSubclass().append(classSubclassProtocolSplit[2][0:2])
                            device.getUsbProtocol().append(classSubclassProtocolSplit[3][0:2])
                        else:
                            device.getUsbClass().append('None')
                            device.getUsbSubclass().append('None')
                            device.getUsbProtocol().append('None')
                        if(len(deviceMfgSplit) >= 1):
                            device.getDeviceMfg().append(deviceMfgSplit[1])
                        else:
                            device.getDeviceMfg().append('None')
                        try:
                            device.getParentIdPrefix().append(serialNumberKey.value("ParentIdPrefix").value())
                        except:
                            print("missingParentIdPrefix exception at (i,j) = (", i, ",", j, ") with serial number key:", device.getSerialNumber()[-1])
                            device.getParentIdPrefix().append('None')
                        device.getServiceName().append(serialNumberKey.value("Service").value())
                        device.getCapabilities().append(serialNumberKey.value("Capabilities").value())
                        
                        properties1Key = serialNumberKey.subkey("Properties").subkey("{540b947e-8b40-45bc-a8a2-6a0b894cbda2}")
                        try:
                            properties1_4Key = properties1Key.subkey("0004")
                            device.getDeviceName().append(((properties1_4Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties1Key.path(), "\\0004] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceName().append('None')
                        
                        try:
                            properties1_7Key = properties1Key.subkey("0007")
                            device.getDeviceConfigurationId().append(((properties1_7Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties1Key.path(), "\\0007] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceConfigurationId().append('None')
    
                        try:
                            properties1_AKey = properties1Key.subkey("000A")
                            device.getBiosDeviceName().append(((properties1_AKey.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties1Key.path(), "\\000A] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getBiosDeviceName().append('None')
                        
                        properties2Key = serialNumberKey.subkey("Properties").subkey("{a8b865dd-2e3d-4094-ad97-e593a70c75d6}")
                        try:
                            properties2_2Key = properties2Key.subkey("0002")
                            stringDate = dateFromLittleEndian(properties2_2Key.value("").raw_data())
                            device.getDrAssemblyDate().append(stringDate)
                        except:
                            print("keyDoesNotExsist exception [", properties2Key.path(), "\\0002] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDrAssemblyDate().append('None')
    
                        try:
                            properties2_3Key = properties2Key.subkey("0003")
                            device.getDrVersion().append(((properties2_3Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties2Key.path(), "\\0003] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDrVersion().append('None')
                        
                        try:
                            properties2_4Key = properties2Key.subkey("0004")
                            device.getDrDescription().append(((properties2_4Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties2Key.path(), "\\0004] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDrDescription().append('None')  
                        
                        try:
                            properties2_5Key = properties2Key.subkey("0005")
                            device.getDrInfPath().append(((properties2_5Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties2Key.path(), "\\0005] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDrInfPath().append('None')
                        
                        try:
                            properties2_6Key = properties2Key.subkey("0006")
                            device.getDrInfSection().append(((properties2_6Key.value("").raw_data()).replace(b'\x00', b'')).decode('utf-8'))
                        except:
                            print("keyDoesNotExsist exception [", properties2Key.path(), "\\0006] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDrInfSection().append('None')
                        
                        properties3Key = serialNumberKey.subkey("Properties").subkey("{83da6326-97a6-4088-9453-a1923f573b29}")
                        try:
                            properties3_64Key = properties3Key.subkey("0064")
                            stringDate = dateFromLittleEndian(properties3_64Key.value("").raw_data())
                            device.getDeviceInstallDate().append(stringDate)
                        except:
                            print("keyDoesNotExsist exception [", properties3Key.path(), "\\0064] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceInstallDate().append('None')
                        
                        try:
                            properties3_65Key = properties3Key.subkey("0065")
                            stringDate = dateFromLittleEndian(properties3_65Key.value("").raw_data())
                            device.getDeviceFirstInstallDate().append(stringDate)
                        except:
                            print("keyDoesNotExsist exception [", properties3Key.path(), "\\0065] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceFirstInstallDate().append('None')
                        
                        try:
                            properties3_66Key = properties3Key.subkey("0066")
                            stringDate = dateFromLittleEndian(properties3_66Key.value("").raw_data())
                            device.getDeviceLastArrivalDate().append(stringDate)
                        except:
                            print("keyDoesNotExsist exception [", properties3Key.path(), "\\0066] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceLastArrivalDate().append('None')
                        
                        try:
                            properties3_67Key = properties3Key.subkey("0067")
                            stringDate = dateFromLittleEndian(properties3_67Key.value("").raw_data())
                            device.getDeviceLastRemovalDate().append(stringDate)
                        except:
                            print("keyDoesNotExsist exception [", properties3Key.path(), "\\0067] \n \t at (i,j) = (", i, ",", j, ") \n \t with serial number key:", device.getSerialNumber()[-1])
                            device.getDeviceLastRemovalDate().append('None')
                    
                    except:
                        print("assignment exception at (i,j) = (", i, ",", j, ") with serial number key:", device.getSerialNumber()[-1]);
                usbFinalList.append(device)
        except:
            print("exception at i = ", i)
            continue;
    return usbFinalList
