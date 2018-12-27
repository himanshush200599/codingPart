import math
def checkprime(x):
    if x==1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0:
        return False
    if x%3==0:
        return False
    if x<9:
        return True

    k=5
    f=math.floor(math.sqrt(x))

    while(k<=f):
        if(x%k==0):
            return False
        if(x%(k+2)==0):
            return False
        k+=6
    return True
y=1
a=[]
x=0
while(True):
    y+=1
    if checkprime(y):
        a.append(y)
        x+=1
    if(x==10001):
        break
print(a[-1])
