def isPythagoras(a,b,c) :
    if(a**2+b**2 == c**2) :
        return True
    else :
        return False
a1 = 3
a2 = 4
a3 = 8
a4 = 7 
b1 = 4
b2 = 9
b3 = 6
b4 = 8
c1 = 5
c2 = 12
c3 = 10
c4 = 11

print("a =", a1, ", b =", b1, ", c =", c1, "->" , isPythagoras(a1,b1,c1))
print("a =", a2, ", b =", b2, ", c =", c2, "->" , isPythagoras(a2,b2,c2))
print("a =", a3, ", b =", b3, ", c =", c3, "->" , isPythagoras(a3,b3,c3))
print("a =", a4, ", b =", b4, ", c =", c4, "->" , isPythagoras(a4,b4,c4))