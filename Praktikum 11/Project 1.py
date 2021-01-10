from datetime import *

def diffDate(x) :
    tanggal  = x.split("-")
    detailtgl = []

    for i in tanggal :
        detailtgl.append(int(i))

    inputantgl = date(detailtgl[0], detailtgl[1], detailtgl[2])
    sekarang = datetime.date(datetime.now())
    Selisih = inputantgl - sekarang
    hari = Selisih.days

    return hari

try :
    tanggal = input("Masukkan tanggal yang akan dicari selisihnya (yyyy-mm-dd): ")
    hasil   = diffDate(tanggal)
    print("Selisih tanggal",tanggal,"dengan hari ini adalah",hasil,"hari")
except ValueError :
    print("Format tanggal salah!")