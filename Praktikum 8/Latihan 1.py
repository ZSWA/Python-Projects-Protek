listA = [1, 5, 6, 3, 6, 9, 11, 20, 12]
listB = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print("isi dari list A", listA)
print("isi dari list B", listB)

listA.insert(3, 10)
listB.insert(2, 15)
print("isi list A setelah diinsert bilangan 10 pada index ke 3 :\n", listA)
print("isi list B setelah diinsert bilangan 15 pada index ke 2 :\n", listB)

listA.append(4)
listB.append(8)
print("isi list A setelah diinsert bilangan 4 pada terakhir :\n", listA)
print("isi list B setelah diinsert bilangan 8 pada terakhir :\n", listB)

listC = listA[:7]
listD = listB[2:9]
print("isi list C yang berisi sublist A :\n", listC)
print("isi list D yang berisi sublist B :\n", listD)

listE = []
for a in range(len(listC)):
    listE += [listC[a]+listD[a]]
print("isi list E yang berisi jumlah list C dan list D :\n", listE)
listE = tuple(listE)
print("isi list E yang telah di ubah menjadi tuple :\n", listE)

minE = min(listE)
maxE = max(listE)
sumE = sum(listE)
print("nilai minimal list E", minE)
print("nilai maximal list E", maxE)
print("nilai sum dari list E", sumE)

myString = "python adalah bahasa pemrograman yang menyenangkan"
print("isi list myString :\n", myString)
myStringSet = set(myString)
print("huruf penyusun myString :\n", myStringSet)
myStringSetList = list(myStringSet)
print("huruf penyusun myString yang telah diubah menjadi list:\n", myStringSetList)
myStringSetList.sort()
print("list myString yang telah di urutkan:\n", myStringSetList)
