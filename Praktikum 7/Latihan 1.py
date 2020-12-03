nama = input("Masukkan nama file : ")
try :
    file = open(nama, "r")
    print("isi dari file", nama, "adalah :")
    print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan")
except :
    print("Ada sesuatu yang salah")