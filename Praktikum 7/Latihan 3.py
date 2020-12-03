print('-------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-------------------------')

lagi = 'y'
jumlah = 0
hitung = 0
while lagi == 'y':
    try:
        bilangan = int(input("Masukkan bilangan bulat : "))
        jumlah += bilangan
        hitung += 1
        lagi = input("Lagi (y/n)?")
    except ValueError:
        print("Bukan bilangan bulat")

rata = jumlah/hitung
if(hitung >= 1):
    print('\n Rata-ratanya adalah', rata)
else:
    print('\n Data tidak diinputkan!')
