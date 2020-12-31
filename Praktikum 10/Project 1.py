try :
    file = open('D:/project1.txt', 'r')
    data = file.readlines()

    genap=[]
    ganjil=[]

    for i in range(len(data)):
        if (int(data[i])%2) == 0:
            genap += [data[i]]  
        else :
            ganjil += [data[i]]
        
    print('Banyak bilangan genap  : ', len(genap))
    print('Banyak bilangan ganjil : ', len(ganjil))
except :
    print("File tidak ditemukan")