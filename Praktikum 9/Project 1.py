def ubahhuruf(teks, a, b) :
    daftar = list(teks)
    hasil = ""
    
    for i in daftar :
        if(i == a) :
            i = b
        hasil = " ".join([hasil,i])
    return hasil

Bahan = input("Masukkan Kalimat : ").upper()
ubah = input("Masukkan huruf yang akan diubah : ").upper()
timpa = input("Masukkan huruf pengganti : ").upper()
print(ubahhuruf(Bahan, ubah, timpa))