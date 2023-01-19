import collections

Person = collections.namedtuple('Person', ['name', 'age'])
person_list=[]

f= open("20230119/input.txt")
for i in f:
    i=i.strip().split(" ")
    #for k in i:
    #    print(k)
    person_list.append(Person(i[0], int(i[1])))
f.close()

_sum=0
for i in person_list:
    _sum+=i.age

print(_sum/len(person_list))




nevek=[]
korok=[]


f= open("20230119/input.txt")
for i in f:
    i=i.strip().split(" ")
    nevek.append(i[0])
    korok.append(int(i[1]))
f.close()

szum=0
for i in korok:
    szum+=i
print("Átlag: "+str(szum/len(korok)))








