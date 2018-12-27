#largest prime factor of a number
def isPrime(no):
    for i in range(2,no):
        if no%i==0:
            return False
    else:
        return True

n =  int(input())
ans = 0
for i in range(1,n+1):
    if n%i==0:
        if isPrime(i):
            if ans<i:
                ans = i
print(ans)
