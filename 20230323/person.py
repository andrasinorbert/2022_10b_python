class Person():
    # constructor
    def __init__(self,_id, _nev, _kor, _magassag):
        self.id=_id
        self.nev=_nev
        self.kor=_kor
        self.magassag=_magassag
        
    def __repr__(self):
        return f"{self.id}, {self.nev}, {self.kor}, {self.magassag}"
    
    def __str__(self):
        return f"{self.id}, {self.nev}, {self.kor}, {self.magassag}"
    
    def kiir(self):
        print(f"név: {self.nev}")