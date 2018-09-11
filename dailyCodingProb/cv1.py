n = int(input())
nf = []
nps = []
k=[]
for i in range(2,n//2):
    if n%i==0:
        nf.append(i)
nf.append(n)
for i in nf:
    if round(i ** 0.5) ** 2 == i:
        nps.append(i)
        nf.remove(i)
z = len(nf)
for i in range(z):
    for j in range(len(nps)):
        if nf[i]%nps[j]==0:
            k.append(nf[i])
for i in k:
    nf.remove(i)

print(len(nf))
