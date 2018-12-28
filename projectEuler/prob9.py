
c=0
m=2
while True:
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(a==0 or b==0 or c==0):
            break
        if (a+b+c == 1000):
            print(a*b*c)
            break
    m=m+1
