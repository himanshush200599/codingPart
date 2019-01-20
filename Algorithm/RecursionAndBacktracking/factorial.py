#first program of this recursion series
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(997))
#  997 is limit in python of above program -,-
