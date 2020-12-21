mhs = ['K001:ROSIHAN ARI        :1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN        :2005-01-28:KARANGANYAR']

#========================
print("="*80)
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(20), "TGL LAHIR".ljust(20), " TEMPAT LAHIR".ljust(20))
print("-"*80)
#------------------------

for jumlah in mhs :
    datasplit = jumlah.split(":")
    NIM = datasplit[0]
    Nama = datasplit[1]
    tgl = datasplit[2]
    tglSplit       = tgl.split('-')
    formatTglLahir = "{2}/{1}/{0}".format(tglSplit[0],tglSplit[1],tglSplit[2])
    tempatLahir        = datasplit[3]

    print(NIM.ljust(10), Nama.ljust(20), formatTglLahir.ljust(20), tempatLahir.ljust(20))

print("-"*80)
#---------------------------