from Vehicle import Vehicle

class Ship(Vehicle):
    # constructor
    def __init__(self):
        super().__init__()
        self.__age = 0                      
        self.__type = ""                    
        self.__country= ""   
    
    # setter and getter
    def setShip(self, name, fuelType, maxPassengers, age, type, country):
        self.setVehicle(name, fuelType, maxPassengers)
        self.__age = age
        self.__type = type
        self.__country = country

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setCountryOfManufactur(self, country):
        self.__country = country

    def getCountryOfManufacture(self):
        return self.__country

    # method
    def printShip(self):
        self.printVehicle()
        print("Umur Kapal (tahun) : " + str(self.__age))
        print("Tipe Kapal : " + str(self.__type))
        print("Negara Asal : " + str(self.__country))
        self.move()