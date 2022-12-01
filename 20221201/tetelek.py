def Sorozatszamitas(X:list, func, s=0 ):
    """írok valamit
    func: lfbkbfleé
    """
    for i in range(len(X)):
        s=func(s, X[i])
    return s

def Megszamlalas(X, func):
    c=0
    for i in range(len(X)):
        if(func(X[i])):
            c+=1
    return c
def SzelsoertekKivalasztas(X, func):
    Index=0
    Ertek=X[0]
    for i in range(1, len(X)):
        if (func(X[i], Ertek)):
            Ertek=X[i]
            Index=i
    return (Index,Ertek)
