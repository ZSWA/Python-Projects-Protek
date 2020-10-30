ganjil = 0
ganjil+=1
jumlah = 1
a=1
while (ganjil<100) :
    if ganjil == 99 :
        print(ganjil)
        break
    else :
        print(ganjil)
        ganjil+=2
        jumlah += ganjil
        a+=1

print("banyaknya bilangan ganjil = ",a)
print("Jumlah seluruh bilangan ganjil" ,jumlah)