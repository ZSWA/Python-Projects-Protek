def starFormation1(baris) :
    i=0
    while(i<baris) :
        j =i+1
        while (j>0) :
            print("*", end="")
            j-=1
        print("")
        i+=1

formasi = int(input("Masukkan jumlah formasi :"))
starFormation1(formasi)

def starFormation2(baris) :
    i=0
    while(i<baris) :
        j =i+1
        while (j<baris) :
            print("*", end="")
            j+=1
        print("*")
        i+=1
    return i
formasi2 = int(input("Masukkan jumlah formasi :"))
starFormation2(formasi2)

def starFormation3(baris) :
    if(baris % 2 == 0) :
        starFormation1(baris//2)
    else:
        starFormation1(baris//2+1)
    starFormation2(baris//2)

formasi3 = int(input("Masukkan jumlah formasi :"))
starFormation3(formasi3)