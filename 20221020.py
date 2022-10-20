# Harmonikus közép

X=[4,2,16] # 1/4 1/2 1/16  => 3/((4+8+1)/16)=3/(13/16)
s=0
for i in range(len(X)):
    s+= 1/X[i]
valasz=len(X) / s
print("A számok harmonikus közepe:", valasz)