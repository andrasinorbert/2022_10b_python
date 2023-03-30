

nev="Julcsi"
kor=13
magassag=160

szotar={
    "nev":"Julcsi",
    "kor": 13,
    "magassag": 160
}

for i in szotar:
    print(f"{i}: {szotar[i]}")
    
class Person():
    # constructor
    def __init__(self,_nev, _kor, _magassag):
        self.nev=_nev
        self.kor=_kor
        self.magassag=_magassag
        
    def __repr__(self):
        return f"{self.nev}, {self.kor}, {self.magassag}"
    
    def __str__(self):
        return f"{self.nev}, {self.kor}, {self.magassag}"
    
    def kiir(self):
        print(f"név: {self.nev}")

lista=[]
for i in range(13, 20):
    lista.append(Person(f"Klára{i}", i, 150))

print(lista)

for i in lista:
    i.kiir()
