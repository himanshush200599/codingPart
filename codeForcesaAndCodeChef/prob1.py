n = int(input())
st = input()
ans = ''
ans  = ans + st[0]
i = 2
while i<=n and n>0:
    ans = ans + st[i]
    i*=2
    i+=1

print(ans)
