print("hello")

t=[3,5,8,10,3,6]

# print(sum(t))

# Összegzés (Sorozatszámítás) tétele
sum=0
for i in t:
    sum+=i

print(sum)

sum=0
i=0
while i<len(t):
    sum+=t[i]
    i+=1

print(sum)

print("átlag:", sum/len(t))
print("kerekítve:", round(sum/len(t)))
print("lefele kerekítve:", int(sum/len(t)))

num= 6.4

print("felfele kerekítés:", int(num)+1)



