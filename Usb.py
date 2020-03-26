class Usb:
    
    def __init__(self, keyID):
        self._keyID = keyID
        self._serialNumber = []
        self._description = []
        self._usbClass = []
        self._usbSubclass = []
        self._usbProtocol = []
        self._parentIdPrefix = []
        self._serviceName = []
        self._capabilities = []
        self._deviceName = []
        self._drVersion = []
        self._drAssemblyDate = []
        self._drInfPath = []
        self._drInfSection = []
        self._drDescription = []
        self._deviceMfg = []
        self._deviceConfigurationId = []
        self._biosDeviceName = []
        self._deviceInstallDate = []
        self._deviceFirstInstallDate = []
        self._deviceLastArrivalDate = []
        self._deviceLastRemovalDate = []
    
    def getKeyID(self):
        return self._keyID
    
    def setKeyID(self, keyID):
        self._keyID = keyID
    
    def getDeviceName(self):
        return self._deviceName
    
    def setDeviceName(self, deviceName):
        self._deviceName = deviceName
    
    def getDescription(self):
        return self._description
    
    def setDescription(self, description):
        self._description = description
    
    def getVendorID(self):
        return self._vendorID
    
    def setVendorID(self, vendorID):
        self._vendorID = vendorID
    
    def getProductID(self):
        return self._productID
    
    def setProductID(self, productID):
        self._productID = productID
    
    def getUsbClass(self):
        return self._usbClass
    
    def setUsbClass(self, usbClass):
        self._usbClass = usbClass
    
    def getUsbSubclass(self):
        return self._usbSubclass
    
    def setUsbSubclass(self, usbSubclass):
        self._usbSubclass = usbSubclass
    
    def getUsbProtocol(self):
        return self._usbProtocol
    
    def setUsbProtocol(self, usbProtocol):
        self._usbProtocol = usbProtocol
    
    def getParentIdPrefix(self):
        return self._parentIdPrefix
    
    def setParentIdPrefix(self, parentIdPrefix):
        self._parentIdPrefix = parentIdPrefix
    
    def getServiceName(self):
        return self._serviceName
    
    def setServiceName(self, serviceName):
        self._serviceName = serviceName
    
    def getDrAssemblyDate(self):
        return self._drAssemblyDate
    
    def setDrAssemblyDate(self, drAssemblyDate):
        self._drAssemblyDate = drAssemblyDate
    
    def getDrDescription(self):
        return self._drDescription
    
    def setDrDescription(self, drDescription):
        self._drDescription = drDescription
    
    def getDrVersion(self):
        return self._drVersion
    
    def setDrVersion(self, drVersion):
        self._drVersion = drVersion
    
    def getDrInfPath(self):
        return self._drInfPath
    
    def setDrInfPath(self, drInfPath):
        self._drInfPath = drInfPath
    
    def getDrInfSection(self):
        return self._drInfSection
    
    def setDrInfSection(self, drInfSection):
        self._drInfSection = drInfSection
    
    def getCapabilities(self):
        return self._capabilities
    
    def setCapabilities(self, capabilities):
        self._capabilities = capabilities
    
    def getSerialNumber(self):
        return self._serialNumber
    
    def setSerialNumber(self, serialNumber):
        self._serialNumber = serialNumber
    
    def getDeviceMfg(self):
        return self._deviceMfg
    
    def setDeviceMfg(self, deviceMfg):
        self._deviceMfg = deviceMfg
    
    def getDeviceConfigurationId(self):
        return self._deviceConfigurationId
    
    def setDeviceConfigurationId(self, deviceConfigurationId):
        self._deviceConfigurationId = deviceConfigurationId
    
    def getBiosDeviceName(self):
        return self._biosDeviceName
    
    def setBiosDeviceName(self, biosDeviceName):
        self._biosDeviceName = biosDeviceName
    
    def getDeviceInstallDate(self):
        return self._deviceInstallDate
    
    def setDeviceInstallDate(self, deviceInstallDate):
        self._deviceInstallDate = deviceInstallDate
    
    def getDeviceFirstInstallDate(self):
        return self._deviceFirstInstallDate
    
    def setDeviceFirstInstallDate(self, deviceFirstInstallDate):
        self._deviceFirstInstallDate = deviceFirstInstallDate
    
    def getDeviceLastArrivalDate(self):
        return self._deviceLastArrivalDate
    
    def setDeviceLastArrivalDate(self, deviceLastArrivalDate):
        self._deviceLastArrivalDate = deviceLastArrivalDate
    
    def getDeviceLastRemovalDate(self):
        return self._deviceLastRemovalDate
    
    def setDeviceLastRemovalDate(self, deviceLastRemovalDate):
        self._deviceLastRemovalDate = deviceLastRemovalDate

    def toString(self):
        usb_x = ""
        usb_x += "ID: " + str(self.getKeyID()) + " - VID_" + self.getVendorID() + "&PID_" + self.getProductID() + " - Serial Number: " + self.getSerialNumber()[0] + "\n"
        usb_x += "Device Name: " + self.getDeviceName()[0] + " - Description: " + self.getDescription()[0] + "\n"
        usb_x += "Class: " + self.getUsbClass()[0] + " - Subclass: " + self.getUsbSubclass()[0] + " - Protocol: " + self.getUsbProtocol()[0] + "\n"
        usb_x += "ParentIdPrefix: " + self.getParentIdPrefix()[0] + " - Service Name: " + self.getServiceName()[0] + "\n"
        usb_x += "Driver Assemlby Date: " + str(self.getDrAssemblyDate()[0]) + " - Driver Description: " + self.getDrDescription()[0] + " - Driver Version: " + self.getDrVersion()[0] + "\n"
        usb_x += "Driver Inf Path: " + self.getDrInfPath()[0] + " - Driver Inf Section: " + self.getDrInfSection()[0] + "\n"
        usb_x += "Capabilities: " + str(self.getCapabilities()[0]) + " - Device Mfg: " + self.getDeviceMfg()[0] + "\n"
        usb_x += "Device Configuration ID: " + self.getDeviceConfigurationId()[0] + " - BIOS Device Name: " + self.getBiosDeviceName()[0] + "\n"
        usb_x += "Device Install Date: " + str(self.getDeviceInstallDate()[0]) + "\n"
        usb_x += "Device First Install Date: " + str(self.getDeviceFirstInstallDate()[0]) + "\n"
        usb_x += "Device Last Arrival Date: " + str(self.getDeviceLastArrivalDate()[-1]) + "\n"
        usb_x += "Device Last Removal Date: " + str(self.getDeviceLastRemovalDate()[-1]) + "\n"
        usb_x += "\n========================================================\n\n\n\n"
        return usb_x