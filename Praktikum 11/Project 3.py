from datetime import *

def statuspengembalian(x) :
    file = open("datapinjam.txt","r")
    baca = file.readlines()
    hasil = " "

    for i in range(len(baca)) :
        if(x in baca[i]) :
            hasil = baca[i].split('|')
            status  = 'ada'
            break
        else :
            status = 'tidak ada'
            continue
    
    if(status == "ada"):
        batas = hasil[4].replace('\n','')
        tgls = batas.split("-")
        tgl = date (year = int(tgls[0]), month = int(tgls[1]), day= int(tgls[2]))
        sekarang = datetime.date(datetime.now())
        terlambat = int((sekarang - tgl).days)

        if(terlambat <= 0):
            status = "Tidak Terlambat"
            denda         = "Tidak Ada Denda"
        elif(terlambat > 0):
            status = str(terlambat) + " hari"
            denda         = "Rp " + str(terlambat*2000)

        print("Data Peminjaman Buku")
        print("Kode Member                 : ", hasil[0])
        print("Nama Member                 : ", hasil[1])
        print("Judul Buku                  : ", hasil[2])
        print("Tanggal Mulai Peminjaman    : ", hasil[3])
        print("Tanggal Maks Peminjaman     : ", batas)
        print("Tanggal Pengembalian        : ", sekarang)
        print("Terlambat                   : ", status)
        print("Denda                       : ", denda)
    else:
        print("Data mahasiswa tidak ditemukan")

kode = input("Masukkan kode member : ").upper()
statuspengembalian(kode)