rendszamok=[]
adatok=[]

def adatokBeolvasása():
    f=open("20230216\\fuvarok.txt")
    sorok=f.readlines()
    f.close()
    for i in sorok:
        t=i.split(" ")
        rendszamok.append(t[0])
        adat=[]
        for j in range(1,len(t)):
            adat.append(int(t[j]))
        adatok.append(adat)
        
adatokBeolvasása()
print(rendszamok)
print(adatok)