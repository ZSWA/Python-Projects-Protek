try:
    hitung = int(input("Banyak input : "))
    data = []
    perulangan = 0
    
    while perulangan < hitung :
        bilangan = int(input("Masukkan bilangan bulat : "))
        print("Angka", bilangan, "dimasukkan")
        data.append(bilangan)
        perulangan += 1
    
    data.sort(reverse=True)
    print("Hasil inputan dengan urutan besar ke kecil :\n" ,data)
except ValueError:
    print("Data yang dimasukkan bukan angka")