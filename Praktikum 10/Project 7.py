def decrypt(text, jumlah):
    listTeks = list(teks)
    for x in range(len(listTeks)): 
        if(listTeks[x] != ' '):
            if(ord(listTeks[x]) - jumlah >= 65):
                asciiCode = ord(listTeks[x])
                decryption = asciiCode - jumlah
                listTeks[x] = chr(decryption)
            else :
                asciiCode = ord(listTeks[x])
                decryption = (asciiCode + 26) - jumlah
                listTeks[x] = chr(decryption)
        else :  
            continue

    hasil = ''.join(listTeks)
    return hasil


try :
    
    teks = input('Inputkan teks yang akan didekripsi :')
    jml = int(input('Berapa jumlah geseran pada didekripsi :'))

    hasil = decrypt(teks, jml)
    print('\nHasil enkripsi dari teks {0} yaitu : {1}'.format(teks, hasil))

except ValueError :
    print('Inputan error (bilangan bulat)')