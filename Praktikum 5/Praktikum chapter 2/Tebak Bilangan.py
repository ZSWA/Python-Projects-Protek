from random import randint
import time

print("Hai, Selamat datang di Permainan Tebak Angka, Coba tebak angka yang saya simpan ^-^)/")
score = 100
print ("Score Awal Anda = ", score)
Tebak = randint(1, 100)
print(Tebak)
time.sleep(2)
print("Sedang mendapatkan angka...")

time.sleep(2)
print("Angka sudah didapatkan, sekarang tebak angkanya!")

time.sleep(1)
Jawab = int(input("Masukkan Jawaban Anda : "))
if (score<0) :
    print("Game Over")
else :           
    while (Jawab<Tebak) :
        print ("Jawaban anda terlalu kecil")
        print ("---------------------------------------")
        Jawab = int(input("Masukkan Jawaban Anda : "))
        score-=2

    while (Jawab>Tebak) :
        print ("Jawaban anda terlalu Besar")
        print ("---------------------------------------")
        Jawab = int(input("Masukkan Jawaban Anda : "))
        score-=2

    if (Jawab == Tebak) :
        print ("---------------------------------------")
        print("Selamat Jawaban anda Benar ^-^)/")
        print("Score anda = ", score)