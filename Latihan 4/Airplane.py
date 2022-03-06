from Vehicle import Vehicle

class Airplane(Vehicle):
    # contructor
    def __init__(self):
        super().__init__()
        self.__age = 0          
        self.__type = ""        
        self.__wingsLength = 0  

    # setter and getter
    def setAirplane(self, name, fuelType, maxPassengers, age, type, wingsLength):
        self.setVehicle(name, fuelType, maxPassengers)
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return self.__wingsLength

    # method
    def printAirplane(self):
        self.printVehicle()
        print("Umur Pesawat (Tahun) : " + str(self.__age))
        print("Tipe Pesawat : " + str(self.__type))
        print("Panjang Sayap (Meter): " + str(self.__wingsLength))
        self.move()