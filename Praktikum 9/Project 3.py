def bintang(n):
    atas = n/2-0.5
    i = 0
    tengah = "*"*n
    while(i<atas) :
        star = "*"*(i*2+1)
        print(star.center(10))
        i+=1
    print(tengah.center(10))
    while(i>0) :
        stars = "*"*(i*2-1)
        print(stars.center(10))
        i-=1
try :
    a = int(input("Masukkan banyak bintang : "))
    if (a % 2 == 0) :
        print("Bukan bilangan ganjil")
    else  :
        bintang(a)
except ValueError:
    print("Data yang dimasukkan salah")