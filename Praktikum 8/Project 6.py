def sortStringByChar(x):
    x.sort(reverse=True, key=len)
    return x

try :
    hitung = int(input("Banyak input : "))
    data = []
    perulangan = 0
    
    while perulangan < hitung :
        Mahasiswa = input("Masukkan data mahasiswa : ")
        print("Data", Mahasiswa, "dimasukkan")
        data.append(Mahasiswa)
        perulangan += 1
    
    sorteddata = sortStringByChar(data)
    print (sorteddata)
except ValueError :
    print("Data yang simasukkan salah")