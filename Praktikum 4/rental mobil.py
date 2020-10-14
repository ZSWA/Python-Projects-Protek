import math

print("-----------------------------")
print("Program Penghitung Tarif Sewa")
print("-----------------------------")

sewa1 = 200000
print("Tarif sewa pertama kali  : ", sewa1 ,"untuk 12 jam")
sewalanjut = 10000
print("Tarif sewa selanjutnya   : ", sewalanjut , "untuk 1 jam")

#waktu sewa
WaktuMulai = 06.00
WaktuSelesai = 23.50
WaktuSewa = math.floor(WaktuSelesai-WaktuMulai)
print("Waktu sewa :", WaktuMulai ,"-" , WaktuSelesai)

#operasi perhitungan
Waktusewa1 = 12
Waktusewatambahan = WaktuSewa - Waktusewa1

biayaTambahan = Waktusewatambahan*sewalanjut
TotalBiaya = sewa1 + biayaTambahan

#kesimpulan
print("Biaya yang harus dibayar", TotalBiaya)