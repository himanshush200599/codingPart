def func(s):
    l=list(s)
    n=len(s)
    k=[]
    if(l[0]!=l[1]):
        k.append(l[0])
    for i in range(1,n-1):
        if(l[i]!=l[i-1] and l[i]!=l[i+1]):
            k.append(l[i])
    if(l[n-2]!=l[n-1]):
        k.append(l[n-1])
    m=len(k)
    for i in range(1,m):
        if(k[i]==k[i-1]):
            return func(k)
    print(''.join(k))




t=int(input())
for i in range(t):
    s=input()
    func(s)
