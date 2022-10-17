list=[2,4,6,8]
l2=list
print(l2)
l2[1]=10
print(l2)
print(list)

l3=list[:]
l3[0]=5
print(list)
print(l3)