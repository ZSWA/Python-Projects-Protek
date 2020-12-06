def dataStat(x):
    varX = tuple(x)
    a = sum(varX) / len(varX)
    b = max(varX)
    c = min(varX)
    return [a, b, c]

try:
    hitung = int(input("Banyak input : "))
    data = []
    perulangan = 0
    
    while perulangan < hitung :
        bilangan = int(input("Masukkan bilangan bulat : "))
        print("Angka", bilangan, "dimasukkan")
        data.append(bilangan)
        perulangan += 1
    
    hasil = dataStat(data)
except ValueError:
    print("Data yang dimasukkan bukan angka")

print("----------------------------------")
print("Rata - rata nilai data", hasil[0])
print("Nilai tertinggi dari list", hasil[1])
print("Nilai terendah dari list", hasil[2])