def dec2hex(num):
    if num == 0:
        return 0
    ans = ""
    while num >0:
        ans = str(num%6) + ans
        num //= 6
    return int(ans)
def hexsum(n1):
    n1 = str(n1)
    s = list(map(int,n1.strip(" ")))
    s = sum(s)
    return s

def main():
    n = int(input())
    l = list(map(int,input().split(",")))
    k = []
    c= 0
    for i in l:
        m = dec2hex(i)
        k.append(hexsum(m))
    for i in range(n):
        for j in range(i,n):
            if((k[i]>k[j])):

                c+=1
    print(c)
main() 
