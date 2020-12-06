buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def tampil(data):
    print('Data buah:')
    for i, j in data.items():
        print('- {0} (Harga Rp{1} / kg)'.format(i,j))
        print('')

tampil(buah)
lagi = 'y'
while lagi == 'y':
    print('='*30)
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus buah')
    print('D. Keluar dari program')
    pilih = input("\npilihan menu : ")
    pilihan = pilih.upper()
    if(pilihan == 'A'):
        inputbuah  = input('Masukkan nama buah    : ')
        if(inputbuah in buah):
            print('buah sudah ada dalam daftar')
        else:
            while True:
                try:
                    harga = int(input('Masukkan harga satuan	: '))
                    buah[inputbuah] = harga
                    tampil(buah)    
                    break
                except ValueError:
                    print('data yang anda masukan bukan angka / salah')
                


    elif(pilihan == 'B'):
        tampil(buah)
        total = 0
        beli = 'y'
        while beli == 'y':
            choose = input("\nNama buah yang dibeli : ")
            if(choose in buah):
                while True:
                    try:
                        kg = float(input('Berapa Kg             : '))
                        total += (buah[choose] * kg)
                        beli = input("Beli buah yang lain (y/n) ? ")
                        break
                    except ValueError:
                        print('data yang anda masukan bukan angka / salah')
                
            else:
                print('\n{0} tidak ada dalam daftar buah'.format(choose))

        print('-------------------------------')
        print("Total harga           :",total)
    elif(pilihan == 'C'):
        hapus  = input('Masukkan nama buah yang ingin dihapus : ')
        if(hapus not in buah):
            print('buah {0} tidak ada dalam daftar'.format(hapus))
        else:
            del(buah[hapus])
            print('buah {0} berhasil dihapus dalam daftar'.format(hapus))
            tampil(buah)
    else:
        break