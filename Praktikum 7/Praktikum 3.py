file = open("d:/data2.txt","r")
sum = 0
for data in file:
    try :
        sum += int(data)
    except ValueError:
        continue
print(sum)