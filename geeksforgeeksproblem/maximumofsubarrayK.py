"""
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T
test cases follows.
The first line of each test case contains a single integer 'N' denoting the size of array and the size of
subarray 'k'.
The second line contains 'N' space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum for every subarray of size k.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 100
1 ≤ k ≤ N
0 ≤A[i]<1000

Example:

Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90



"""

for _ in range(t):
    n,k=[int(e) for e in input().split()]
    arr=list(map(int,input().split()))
    for i in range(len(arr)-k+1):
            print(max(arr[i:k+i]),end=" ")
    print()
