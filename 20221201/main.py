import math as m
print(m.pi)

import tetelek as T

def paros_e(a):
    return a%2==0

print(T.Megszamlalas([3,4,5,6], paros_e))

def szorzas(a,b):
    return a*b

print(T.Sorozatszamitas([2,3,4], szorzas, 1))

def osszead(a, b):
    return a+b
print(T.Sorozatszamitas([2,3,4], osszead))


T.Sorozatszamitas()