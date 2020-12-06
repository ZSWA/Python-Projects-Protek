try:
    buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}
    print("Daftar Buah :")
    menu = 0

    for x,y in buah.items():
        menu += 1
        print(menu,".", x , y)
    
    pilih = input("Buah yang akan dibeli : ")
    Pilihan = pilih.lower()

    if(Pilihan in buah):
        berat = float(input("Akan membeli berapa Kg? : "))
        harga = buah[Pilihan]*berat
        print("==========================")
        print("Total harga : Rp.", harga)
    else :
        print("Buah tidak tersedia")
except ValueError:
    print("Data yang anda masukkan salah")