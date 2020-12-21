def bintang(n):
    i = 0
    while(i<n) :
        star = "*"*(i*2+1)
        print(star.center(10))
        i+=1
    
try :
    a = int(input("Masukkan banyak bintang : "))
    bintang(a)
except : 
    print("Inputan bukan angka")