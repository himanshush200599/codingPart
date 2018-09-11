"""
Given an array A your task is to tell at which position the equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of
 elements after it.

Input:
The first line of input contains an integer T denoting the no of test cases then T test cases follow.

First line of each test case contains an integer N denoting the size of the array. Then in the next line are N
space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium
 point exists print -1.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
1
1
5
1 3 5 2 2

Output:
1
3

"""

def equilibrium(arr):
    total_sum = sum(arr)
    leftsum = 0
    for i in range(len(arr)):
        total_sum -= arr[i]

        if leftsum == total_sum:
            return i+1
        leftsum += arr[i]

    return -1


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print (equilibrium(l))
