Cari = input("Masukan NIM yang ingin dicari : ").upper()
file = open('project2.txt','r')

for data in file:
    baca = data.split("|")
    nim = data.split("|")[0]
    if(nim == Cari):
        result = baca
        break
        
if(result):
    print("Data Mahasiswa")
    print("NIM     :", result[0])
    print("Nama    :", result[1])
    print("Alamat  :", result[2])
else:
    print("Data mahasiswa tidak ditemukan")