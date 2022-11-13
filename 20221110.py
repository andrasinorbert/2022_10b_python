# Adott egy számokat tartalmazó A lista és egy B szám.
# Adjunk meg két olyan elemet az A-ból, amelyek szorzata éppen a B!

A = [3,4,5,6,7,8,9]

B= 12

def T1(e):
    global masikszam
    for i in range(len(A)):
        if e*A[i] == B and e!=A[i]:
            masikszam=A[i]
            return True

def T2(e):
    for i in range(len(A)):
        return A[i] if e*A[i] == B and e!=A[i] else 0

i=0
while i<len(A) and not(True if T2(A[i])!=0 else False):
    i=i+1
van=i<len(A)
if van:
    print(f"A két elem szorzata: {A[i]} és {T2(A[i])}")
else:
    print(f"Nincs két ilyen elem")