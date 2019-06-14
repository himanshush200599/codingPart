def NthFibonacci(n):
    init = [0,1]
    counter = 3
    while counter<=n:
        nextFib = init[0]+init[1]
        init[0] = init[1]
        init[1] = nextFib
        counter +=1
    return init[1] if n>1 else init[0]
print(NthFibonacci(500000))

def NthFibonacciRecursion(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return NthFibonacciRecursion(n-1)+NthFibonacciRecursion(n-2)
print(NthFibonacciRecursion(10))
