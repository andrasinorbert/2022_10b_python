def kiir(x):
    print(x)

kiir("satöbbi")
kiir(3)
kiir(3+4)

def osszead(x,y):
    n=x+y
    return n

n=osszead(3,4)
kiir(n)

kiir(osszead(3,4))

def osszegzesTetel(X, func):
    s=0
    for i in range(len(X)):
        s=func(s,X[i])
    return s

l = [2,3,4,5]
x=osszegzesTetel(l,osszead)
print(x)