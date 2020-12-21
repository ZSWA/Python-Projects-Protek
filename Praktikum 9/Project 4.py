import random
def shuffleString(x, n):
    hasil = []
    loop = 0
    while loop < n:
        acak = ''.join(random.sample(x,len(x)))
        if(acak not in hasil):
            hasil += [acak]
            loop += 1
    print(hasil)
    

shuffleString('aku',5)
shuffleString('aku',4)
shuffleString('aku',3)
shuffleString('aku',2)
shuffleString('aku',1)