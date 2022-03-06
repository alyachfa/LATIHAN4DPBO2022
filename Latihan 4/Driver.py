from Person import Person
from Job import Job

class Driver(Person, Job):
    # constructor
    def __init__(self):
        super().__init__()
        self.__licenseID = ""   
        self.__activeUntil = "" 
        self.__vehicleType = "" 

    # setter and getter
    def setDriver(self, nik, name, isMale, nip, companyName, position, licenseID, activeUntil, vehicleType):
        self.setPerson(nik, name, isMale)
        self.setJob(nip, companyName, position)
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID

    def getLicenseID(self):
        return self.__licenseID

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    # method
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print("ID Lisensi : " + str(self.__licenseID))
        print("Aktif Sampai Dengan : " + str(self.__activeUntil))
        print("Tipe Kendaraan : " + str(self.__vehicleType))
        self.sleep()