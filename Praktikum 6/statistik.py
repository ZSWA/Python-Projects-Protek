def sum(*datas):
    jumlah = 0
    for data in datas:
        jumlah += data
    return jumlah

def average(*datas):
    hitung =  0
    for data in datas:
        hitung += 1
    rata = sum(*datas) / hitung
    return rata

def max(*datas):
    maks = datas[0]
    for data in datas:
        if (data>maks) :
            maks = data
    return maks

def min(*datas):
    minimal = datas[0]
    for data in datas:
        if (data<minimal) :
            minimal = data
    return minimal
