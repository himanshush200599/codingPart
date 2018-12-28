#=========================================================================================================#
#                       Seive of Eratosthenes                                                             #
#                         Efficient way to  find prime number                                             #
#=========================================================================================================#

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    sum=0
    for p in range(2, n):
        if prime[p]:
            sum+=p
    print(sum)
SieveOfEratosthenes(2000000)


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
sum = 0
for i in range(2,2000000):
    if checkprime(i):
        sum+=i
print(sum)
