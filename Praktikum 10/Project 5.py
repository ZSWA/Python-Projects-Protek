file = open('project5.txt','r')
text = ""

for bilangan in file:
    try:
        angka = bilangan.split("|")
        result = int(angka[0]) + int(angka[1])
        text += str(result) + "\n"
    except:
        print(bilangan ,"bukan angka")

hasil = open('hasil.txt','w')
hasil.write(text)
hasil.close
