# problem is to  find common element in 3 sorted array
# arrays are in sorted order
# approac is to traverse all  the arrays and  compare them concurrently
# if all are equals thn  print else move forward



def commonElement(a1,a2,a3,n1,n2,n3):
    i,j,k = 0,0,0
    while i<n1 and j<n2 and k<n3:
        if (a1[i] == a2[j] and a2[j] == a3[k]):
            print(a1[i])
            i += 1
            j += 1
            k += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j] < a3[k]:
            j += 1

        else:
            k+=1
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
commonElement(ar1,ar2,ar3,6,5,8)
