n = int(input())
l = list(map(int,input().split()))
res2 = 9283928932
for i in range(n):
    temp = l.pop(i)
    res = max(l) - min(l)
    if res<res2:
        res2 = res
    l = [temp] + l
print(res)
