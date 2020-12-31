def encrypt(text, jumlah):
    listTeks = list(teks)
    for x in range(len(listTeks)):
        if(listTeks[x] != ' '):
            if(ord(listTeks[x]) + jumlah < 90):
                asciiCode = ord(listTeks[x])
                encryption = asciiCode + jumlah
                listTeks[x] = chr(encryption)
            else :
                asciiCode = ord(listTeks[x])
                encryption = (asciiCode + jumlah) - 26
                listTeks[x] = chr(encryption)
        else :  
            continue

    hasil = ''.join(listTeks)
    return hasil


try :
    
    teks = input('Input teks yang akan dienkripsi :')
    jml = int(input('Berapa jumlah geseran enkripsi :'))

    hasil = encrypt(teks, jml)
    print('\nHasil enkripsi dari teks {0} yaitu : {1}'.format(teks, hasil))

except ValueError :
    print('Inputan error (bilangan bulat)')