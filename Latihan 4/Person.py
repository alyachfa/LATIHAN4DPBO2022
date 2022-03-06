class Person:
    # constructor
    def __init__(self):
        self.__nik = ""      
        self.__name = ""     
        self.__gender = ""

    # setter and getter
    def setPerson(self, nik, name, gender):
        self.__nik = nik
        self.__name = name
        self.__gender = gender

    def setNIK(self, nik):
        self.__nik = nik

    def getNIK(self):
        return self.__nik

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setisMale(self, gender):
        self.__gender = gender

    def getisMale(self):
        return self.__gender

    # method
    def sleep(self):
        print(self.__name + " is sleeping....")

    def printPerson(self):
        print("NIK : " + str(self.__nik))
        print("Nama : " + str(self.__name))
        print("Jenis Kelamin :"+ str(self.__gender))