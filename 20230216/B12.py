import random

while True:
    size= input("Add meg a lista méretét [10...20]: ")
    try:
        size=int(size)
        if size >=10 and size <=20:
            break
        else:
            print("Hibás adatbevitel! Próbáld újra!")
    except:
        print("Hibás adatbevitel! Próbáld újra!")

elemek=[]

for i in range(size):
    elemek.append(random.randint(1,5))

print("A lista tartalma:",elemek)


print("A listában lév ̋o elemek összege:", sum(elemek))

maxertek=elemek[0]
maxindex=0
for i in range(len(elemek)):
    if maxertek<elemek[i]:
        maxertek=elemek[i]
        maxindex=i

print("A listában lév ̋o legnagyobb elem: "+str(maxertek)+", helye: "+str(maxindex+1)+". pozíció")
