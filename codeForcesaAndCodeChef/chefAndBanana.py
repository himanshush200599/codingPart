from math import ceil
def is_possible(a, val, h):
    ct = 0
    for elem in a:
        ct += ceil(elem / val)
    return ct <= h


def binarySearch(n, h, a):
    mmin = 1
    mmax = max(a)

    while mmin <= mmax:
        mid = (mmin + mmax) // 2
        if is_possible(a, mid, h):
            mmax = mid - 1
        else:
            mmin = mid + 1

    return mmin


for _  in range(int(input())):
    n, h = map(int,input().split())
    a = list(map(int,input().split()))
    ans = binarySearch(n, h, a)
    print(ans)
