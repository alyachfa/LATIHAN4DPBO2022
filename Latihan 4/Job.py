class Job:
    # constructor
    def __init__(self):
        self.__nip = ""         
        self.__companyName = "" 
        self.__position = ""    

    # setter and getter
    def setJob(self, nip, companyName, position):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position

    def setNIP(self, nip):
        self.__nip = nip
    
    def getNIP(self):
        return self.__nip

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCompanyName(self):
        return self.__companyName

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position
    
    # method
    def printJob(self):
        print("NIP : " + str(self.__nip))
        print("Nama Perusahaan: " + str(self.__companyName))
        print("Jabatan : " + str(self.__position))