"""
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and

 selling in those days.

Input:
First line contains number of test cases T. Each test case contain the integer value 'N' denoting days followed
 by an array of stock prices in N days.
Output:
The maximum profit is displayed as shown below. And if there is no profit then print "No Profit".


Constraints:
1 <=T<= 100
2 <=N<= 100
1 <=arr[i]<= 10000


Example

Input:
2
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67

Output:

(0 3) (4 6)
(1 4) (5 9)
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    ans=[]
    for j in range(n-1):
        if l[j+1]>l[j]:
            a+=1
            if j==n-2:
                ans.append((j+1-a,j+1))
        else:
            ans.append((j-a,j))
            a=0
    f=0
    for j in ans:
        if j[0]!=j[1]:
            f=1
            print ("("+str(j[0])+" "+str(j[1])+")",end=' ')
    if(f==0):
        print ("No Profit")
        continue
    print()
