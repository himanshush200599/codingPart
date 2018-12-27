# largest palinrome 3 digit number 
def pcheck(x):
    y=int(str(x)[::-1])
    if x==y:
        return True
    else:
        return False

maxn=0
for i in range(100,1000):
    for j in range(100,1000):
        if(pcheck(j*i)):
            if maxn<i*j:
                maxn=i*j
print(maxn)


# largestPalindrome = 0
# a = 999
# while a >= 100
#   b = 999
#   while b >= a
#       if a*b <= largestPalindrome
#           break //Since a*b is always going to be too small
#       if isPalindrome(a*b)
#           largestPalindrome = a*b
#       b = b-1
#   a = a-1
# output largestPalindrome
