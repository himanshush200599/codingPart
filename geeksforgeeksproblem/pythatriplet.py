"""
Given an array of integers, write a function that returns true if there is a triplet (a, b, c)
that satisfies a2 + b2 = c2.

Input:
The first line contains 'T' denoting the number of testcases. Then follows description of testcases.
Each case begins with a single positive integer N denoting the size of array.
The second line contains the N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whtether it is Pythagorean Triplet or not.

"""
def isTriplet(ar,n):
 for i in range(n-1, 1, -1):

    j = 0
    k = i - 1
    while (j < k):

        if (ar[j] + ar[k] == ar[i]):
            return True
        else:
            if (ar[j] + ar[k] < ar[i]):
                j = j + 1
            else:
                k = k - 1

 return False

for _ in range(int(input())):
    n = int(input())
    l = [int(x)**2 for x in input().split()]
    l.sort()
    if(isTriplet(l,n)):
        print("Yes")
    else:
        print("No")
