def kuadrat(bil):
    for i in range(len(bil)):
        bil[i] **= 2
    
    return bil

try:
    hitung = int(input("Banyak input : "))
    data = []
    perulangan = 0
    
    while perulangan < hitung :
        bilangan = int(input("Masukkan bilangan bulat : "))
        print("Angka", bilangan, "dimasukkan")
        data.append(bilangan)
        perulangan += 1
    
    hasil = kuadrat(data)
except ValueError:
    print("Data yang dimasukkan bukan angka")

print(hasil)