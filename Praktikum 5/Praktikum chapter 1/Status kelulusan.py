MTK = int(input("Masukkan nilai Matematika      : "))
BhsIndo = int(input("Masukkan nilai Bahasa Indonesia    : "))
IPA = int(input("Masukkan nilai IPA     : "))

print("Status Kelulusan : ", end ="" )
if (MTK>100) or (BhsIndo>100) or (IPA>100) or (MTK<0) or (BhsIndo<0) or (IPA<0) :
    print("Error input")
elif (MTK<70) or (BhsIndo<60) or (IPA<60) :
    print("Tidak Lulus")
    print("Sebab : ")
    if (MTK<70) :
        print("Nilai Matematika Kurang dari 70")
    if (BhsIndo<60) :
        print("Nilai Bahasa Indonesia Kurang dari 60")
    if (IPA<60) :
        print("Nilai IPA kurang dari 60")
else :
    print("Lulus")