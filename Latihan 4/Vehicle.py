class Vehicle:
    # constructor
    def __init__(self):
        self.__name = ""          
        self.__fuelType = ""        
        self.__maxPassengers = 0    
    
    # setter and getter
    def setVehicle(self, name, fuelType, maxPassengers):
        self.__name = name
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getFuelType(self):
        return self.__fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getMaxPassengers(self):
        return self.__maxPassengers

    # method
    def move(self):
        print(str(self.__name) + " is moving...")

    def printVehicle(self):
        print("Nama : " + str(self.__name))
        print("Tipe Bahan Bakar : " + str(self.__fuelType))
        print("Maksimal Penumpang : " + str(self.__maxPassengers) + " Penumpang")