'''
Selection sort , minimum element is push in left side.
'''

def selection(a,n):
    for i in range(n):
        min1 = i
        for j in range(i+1,n):
            if a[min1]>a[j]:
                min1 = j
        a[min1],a[i] = a[i],a[min1]
    print(a)
selection([6,2,1,7,3,2],6)
