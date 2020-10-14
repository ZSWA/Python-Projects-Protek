import math
lklk = input("Jumlah Mahasiswa Laki-laki :")
prmpn = input("Jumlah Mahasiswi Perempuan :")

#jumlah grafik
grlklk = math.floor(int(lklk) / 10)
grprmpn = math.floor(int(prmpn) / 10)

#pembentukan grafik
print("Grafik Mahasiswa laki-laki   :", "*" * grlklk)
print("Grafik Mahasiswa perempuan   :", "*" * grprmpn)