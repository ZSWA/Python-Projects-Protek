from datetime import*

def pinjambuku(kode, nama, judul):
    file = open("datapinjam.txt","a")
    tanggal = datetime.date(datetime.now())
    kembali = tanggal + timedelta(days=7)
    data = []
    data.append(kode)
    data.append(nama)
    data.append(judul)
    data.append(str(tanggal))
    data.append(str(kembali))
    pisah = "|".join(data)
    file.write(pisah+'|'+"\n")

tambah = "Y"
while tambah == "Y" :
    Kode =     input("Masukkan Kode Member  : ").upper()
    Nama =     input("Masukkan Nama Member  : ")
    Judul =    input("Masukkan Judul Buku   : ")
    pinjambuku(Kode, Nama, Judul)
    tambah =   input("Ulangi lagi? (Y/N)    :").upper()
