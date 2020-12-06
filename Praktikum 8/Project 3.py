try :
    hitung = int(input("Banyak input : "))
    data = []
    perulangan = 0
    
    while perulangan < hitung :
        Mahasiswa = input("Masukkan data mahasiswa : ")
        print("Data", Mahasiswa, "dimasukkan")
        data.append(Mahasiswa)
        perulangan += 1
    
    print("Banyak karakter penyusun setiap data :")

    datta = 0
    while datta < len(data):
        setdata = set(data[datta])
        setlistdata = list(setdata)
        lenlistdata = len(setlistdata)
        print(data[datta], "(", lenlistdata, "Karakter )")
        datta += 1
except ValueError:
    print("Data yang dimasukkan salah")