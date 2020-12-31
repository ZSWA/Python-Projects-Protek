try :
    file = open('project2.txt', 'r')
    baca = file.readlines()

    dictt = {}
    listDict = []

    for i in range(len(baca)) :
        data = baca[i].split('|')
        data[2] = data[2].replace('\n', '')
        dictt = {'nim' : data[0], 'nama' : data[1], 'alamat' : data[2]}
        listDict.append(dictt)

    print(listDict)
    file.close()
except :
    print("File tidak ditemukan")