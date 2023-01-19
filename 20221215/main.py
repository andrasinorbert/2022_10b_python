

f= open("20221215/adatok")

for i in f:
    i=i.strip().split(" ")
    for k in i:
        print(k)
    
f.close()