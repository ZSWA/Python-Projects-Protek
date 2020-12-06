def Rerata(data):
    tupleData = tuple(data.values())
    sumData = sum(tupleData)
    hitung = len(tupleData)
    rata = sumData/hitung
    return rata

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
result = Rerata(buah)
print("rata-rata harga satuan dari keseluruhan buah yang ada adalah ", result)
