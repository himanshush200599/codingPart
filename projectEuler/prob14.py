# Longest collatz sequence
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

def countChain(n):
    if n==1:
        return 1
    if n%2==0:
        return 1+countChain(n/2)
    else:
        return 2+countChain((3*n+1)/2)
l=0
answer=-1

for i in range(500000,1000000+1):
    s = countChain(i)
    if s>l:
        l=s
        answer=i
print(l,answer)
