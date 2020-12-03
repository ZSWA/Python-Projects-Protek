nama = input("Masukkan nama file : ")
try:
    file = open(nama,"a")
    Data = input("Data yang mau ditambahkan : ")
    file.write(Data+'\n')

    while True :
        jawab = input("Mau Lagi? (y/n) : ")
        if (jawab == "y") or (jawab == "Y") :
            Data = input("Data yang mau ditambahkan : ")
            file.write(Data+'\n')
        elif (jawab == "n") or (jawab == "N") :
            file.close()
            file = open(nama,"r")
            print("Isi file", nama ,"adalah")
            print(file.read())
            break
        else :
            print("Input salah, tolong masukkan input y atau n")
except FileNotFoundError :
    print("file tidak ditemukan")