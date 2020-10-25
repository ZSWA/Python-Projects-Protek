Kode   = input("Masukkan Kode Karyawan    : ")
Nama   = input("Masukkan Nama Karyawan    : ")
Gol    = input("Masukkan Golongan         : ")
Status = int(input("Masukkan Status           : "))

Anak = 0
Gaji = int
potongan = float
Gajibersih = float

if (Status == 1) :
    Anak = int(input("Masukkan Jumlah Anak      : "))


if  (Gol == "A") or (Gol =="a") :
    Gaji = 10000000
    potongan = 2.5
elif (Gol == "B") or (Gol == "b") :
    Gaji = 8500000
    potongan = 2
elif (Gol == "C") or (Gol == "c") :
    Gaji = 7000000
    potongan = 1.5
elif (Gol == "D") or (Gol == "d") :
    Gaji = 5500000
    potongan = 1
else :
    print("input salah")



PotonganGJ = Gaji * potongan / 100
TunjanganSI = Gaji * 10/100
TunjanganAnak = (Gaji* 5/100) * Anak
if (Status == 2) :
    TunjanganSI = 0
    TunjanganAnak = 0 
GajiKotor = Gaji+TunjanganSI+TunjanganAnak
Gajibersih = GajiKotor - PotonganGJ

print("===================================")
print("Struktur rincian gaji karyawan")
print("-----------------------------------")
print("Nama Karyawan    :", Nama ,"( Kode" , Kode, ")")
print("Golongan         :", Gol)
print("-----------------------------------")
print("Gaji Pokok       : Rp.", Gaji)
print("Tunjangan Istri/Suami : Rp. ", TunjanganSI)
print("Tunjangan Anak   : Rp.", TunjanganAnak)
print("-----------------------------------")
print("Gaji Kotor       : Rp.", GajiKotor)
print("Potongan (",potongan, "%): Rp.", PotonganGJ )
print("-----------------------------------")
print("Gaji Bersih      : Rp.", Gajibersih)



