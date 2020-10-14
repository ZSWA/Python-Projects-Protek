import math
JarakAC = 795
print("Jarak Kota A ke C adalah ", JarakAC , "KM")
PenggunaanPerLiter = 12
print("1 liter bbm dapat digunakan untuk " ,PenggunaanPerLiter, "KM")
konsumsi = JarakAC / PenggunaanPerLiter
print("maka bensin yang diperlukan untuk perjalanan tersebut adalah " ,  konsumsi ,"liter")
Kapasitastangki = 50
print("Kapasitas tangki mobil pak budi adalah" , Kapasitastangki)

#kondisi awal bensin penuh
isibensin = math.ceil((konsumsi-Kapasitastangki) / Kapasitastangki)
print("banyak isi bensin : ", isibensin)