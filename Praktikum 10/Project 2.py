try :
    file = open('project2.txt','a')

    tambah = "Y"
    while ( tambah == "Y") :
        nim = input('Masukkan NIM      : ')
        nama = input('Masukkan Nama Mhs : ')
        alamat = input('Masukkan Alamat   : ')
   
        file.write(nim + '|' + nama + '|' + alamat + '\n')  
        tambah = input('Ulangi input lagi (y/n) : ').upper()
    
        if (tambah == 'Y') :
            continue
        elif (tambah == 'N'):
            break
        else :
            print ('Inputan salah')
            continue
    file.close()

except :
    print("File tidak ditemukan")