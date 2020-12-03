#membuka dan mau membaca file d:/data.txt
try:
    file = open("d:/data.txt","r")
except FileNotFoundError:
    print("File tidak ditemukan")
#baca baris pertama dari file
#simpan ke dalam variabel bil1 sbg integer
bil1 = int(file.readline())

#baca baris pertama dari file
#simpan ke dalam variabel bil2 sbg integer
bil2 = int(file.readline())
bil2 +=2

#hitung dan tampilkan hasil bagi
try :
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2,' sama dengan ', hasil)
except ZeroDivisionError:
    print("Tidak boleh pembagian dengan 0")