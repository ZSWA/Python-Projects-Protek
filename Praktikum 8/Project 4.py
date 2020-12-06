data = ["bayam" , "kangkung", "wortel", "selada"]

def tambah(a):
    tambahdata = input("Data sayur yang ingin dimasukkan :")
    a.append(tambahdata)
    print(tambahdata, "berhasil ditambahkan")

def hapus(b):
    try:
        hapus = input("Data sayur yang ingin dihapus :")
        b.remove(hapus)
        print(hapus, "berhasil dihapus")
    except :
        print("Data tidak ditemukan")

def tampil(c):
    print(c)

tutup = "y"
while tutup.lower() == "y" :
    print("Menu :")
    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur")

    menu = input("Pilih menu :")

    if (menu == "A") or (menu == "a"):
        tambah(data)
    elif (menu == "B") or (menu == "b"):
        hapus(data)
    elif (menu == "C") or (menu == "c"):
        tampil(data)
    
    tutup = input("ingin mengolah data lagi? (y/n)")
