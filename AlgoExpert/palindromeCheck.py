# Recursive solution - Original
def palindromeCheck(l,r,s):
    if s[l]!=s[r] or l>r:
        return False
    if l==r:
        return True
    return palindromeCheck(l+1,r-1,s)

s = "babab"
print(palindromeCheck(0,len(s)-1,s))

# Iterative solution - Original
def palindromeCheck(l,r,s):
    while l<r:
        if s[l]!=s[r]:
            return False
        else:
            l = l+1
            r = r-1
        if l==r:
            return True

s = "baabaab"
print(palindromeCheck(0,len(s)-1,s))
