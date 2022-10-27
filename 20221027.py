def LeghosszabbSzo(szavak):
    MaxIndex=0
    MaxErtek=szavak[0]
    for i in range(len(szavak)):
        c=0
        for j in range(len(szavak[i])):
            c+=1
        if c> len(MaxErtek):
            MaxErtek=szavak[i]
            MaxIndex=i
    return (MaxIndex, MaxErtek)

szavak_1=[ "szamár", "ló", "burzsuj", "kincs"]
szavak_2=["abc", "def","ghz"]
max=LeghosszabbSzo(szavak_2)
print(f"A leghosszabb szó: {max[1]}, ami a {max[0]+1}. szó")
