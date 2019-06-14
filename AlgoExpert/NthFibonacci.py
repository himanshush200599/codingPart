def NthFibonacci(n):
    init = [0,1]
    counter = 3
    while counter<=n:
        nextFib = init[0]+init[1]
        init[0] = init[1]
        init[1] = nextFib
        counter +=1
    return init[1] if n>1 else init[0]
print(NthFibonacci(1000))
