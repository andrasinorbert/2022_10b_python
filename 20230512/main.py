

# 1. feladat

# sorok:
# Kapitály
# Rico
# Kowalsky
# Közlegény
"""
def adatokBeolvasása(inputfile):
    matrix=[]
    #debug=True
    #fájlmegnyitás:
        # f=open(inputfile, "r")
        # input=f.readlines()
        # f.close()
    
    with open(inputfile, "r") as f:
        inputdata=f.readlines()
    
    #print(inputdata)
    for sor in inputdata:
        sorvégnélkül=sor.strip()
        #if debug: print(sorvégnélkül)
        feldarabolt=sorvégnélkül.split(" ")
        #print(feldarabolt)
        ideigleneslista=[]
        for napihal in feldarabolt:
            #print(napihal)
            szamma_alakitott_verzio=int(napihal)
            ideigleneslista.append(szamma_alakitott_verzio)
        matrix.append(ideigleneslista)
    #print(matrix)
    return matrix
ez nem a feladat megoldása itt felül
"""
def adatokBeolvasása(inputfile):
    matrix=[]
    with open(inputfile, "r") as f:
        inputdata=f.readlines()
    for sor in inputdata:
        sorvégnélkül=sor.strip()
        feldarabolt=sorvégnélkül.split(" ")
        matrix.append(feldarabolt)
    print(matrix)
    return matrix

def konvertálás(matrix):
    for sor in range(len(matrix)):
        for napihal in range(len(matrix[sor])):
            matrix[sor][napihal]= int(matrix[sor][napihal])

halak = adatokBeolvasása("20230512/halak.txt")
konvertálás(halak)

print(halak)

# 3. feladat

leg = legtöbbLegkevesebbHal(halak)
print(f"\nLegjobban megkárosított pingvin: {pingvinek[leg[0]]}")
print(f"Legkevésbé megkárosított pingvin: {pingvinek[leg[1]]}")