from Ship import Ship
from Airplane import Airplane
from Driver import Driver

# Menampung dan menampilkan Data Kapal
ship = [Ship() for i in range(0,5)]
ship[0].setShip("Kapal 1", "Diesel", 600, 1, "Kapal Barang", "Korea Selatan")
ship[1].setShip("Kapal 2", "Diesel", 400, 2, "Kapal Barang", "Korea Selatan")
ship[2].setShip("Kapal 3", "Diesel", 600, 3, "Kapal Barang", "Korea Selatan")
ship[3].setShip("Kapal 4", "Diesel", 1200, 4, "Kapal Pesiar", "Korea Selatan")
ship[4].setShip("Kapal 5", "Diesel", 900, 5, "Kapal Pesiar", "Korea Selatan")

print("DATA KAPAL")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Kapal", i+1)
    ship[i].printShip()
    print("===================================================")

print("DATA KENDARAAN")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Kendaraan", i+1)
    ship[i].printVehicle()
    print("===================================================")

# Menampung dan menampilkan Data Pesawat
airplane = [Airplane() for i in range(0,5)]
airplane[0].setAirplane("Pesawat 1", "Aviation Turbine", 300, 1, "Pesawat Terbang Komersial", 30.7)
airplane[1].setAirplane("Pesawat 2", "Aviation Turbine", 300, 2, "Pesawat Terbang Komersial", 31.3)
airplane[2].setAirplane("Pesawat 3", "Aviation Turbine", 300, 3, "Pesawat Terbang Komersial", 30.7)
airplane[3].setAirplane("Pesawat 4", "Aviation Turbine", 300, 4, "Pesawat Terbang Komersial", 31.3)
airplane[4].setAirplane("Pesawat 5", "Aviation Turbine", 300, 5, "Pesawat Terbang Komersial", 30.7)

print("DATA PESAWAT")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Pesawat", i+1)
    airplane[i].printAirplane()
    print("===================================================")

print("DATA KENDARAAN")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Kendaraan", i+1)
    airplane[i].printVehicle()
    print("===================================================")

# Menampung dan menampilkan Data Pengemudi
driver = [Driver() for i in range(0,5)]
driver[0].setDriver("1111111", "Supir 1", "Perempuan", "12345678", "PT. ACF", "Karyawan", "12345678", "10-09-2027", "Mobil")
driver[1].setDriver("2222222", "Supir 2", "Perempuan", "23456781", "PT. ACF", "Karyawan", "23456781", "10-09-2027", "Mobil")
driver[2].setDriver("3333333", "Supir 3", "Laki-Laki", "34567812", "PT. ACF", "Karyawan", "34567812", "10-09-2027", "Mobil")
driver[3].setDriver("4444444", "Supir 4", "Perempuan", "45678123", "PT. ACF", "Karyawan", "45678123", "10-09-2027", "Mobil")
driver[4].setDriver("5555555", "Supir 5", "Laki-Laki", "56781234", "PT. ACF.", "Karyawan", "56781234", "10-09-2027", "Truk")

print("DATA PENGEMUDI")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Pengemudi", i+1)
    driver[i].printDriver()
    print("===================================================")

print("DATA PRIBADI")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Pribadi", i+1)
    driver[i].printPerson()
    print("===================================================")

print("DATA PEKERJAAN")
print("---------------------------------------------------")
for i in range(0,5):
    print("Data Pekerjaan", i+1)
    driver[i].printJob()
    print("===================================================")