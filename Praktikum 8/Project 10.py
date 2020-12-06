buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
print("Daftar Buah :")
menu = 0

for x,y in buah.items():
    menu += 1
    print(menu,".", x , y)

harga = 0
while True:
    try:
        pilih = input("Buah yang akan dibeli : ")
        Pilihan = pilih.lower()

        if(Pilihan in buah):
            berat = float(input("Akan membeli berapa Kg? : "))
            harga += buah[Pilihan]*berat
            lagi = input("Beli buah yang lain  (y/n) : ")
            if (lagi == "y") :
                continue
            elif (lagi == "n") :
                break
            else :
                print("Input yang anda masukkan salah")
                print("Menghitung total")
                break
        else :
            print("Buah tidak tersedia")
    except:
        print("Data yang anda masukkan salah")
print("==========================")
print("Total harga : Rp.", harga)