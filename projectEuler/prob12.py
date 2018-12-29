import time
start = time.time()
n = 76576488

c = 0
while c<500:

    c = 0
    tn = int((n*(n+1))/2)
    for i in range(1,tn+1):
        if tn%i==0:
            c+=1
            if c>=500:
                print(tn)
                break
    print(time.time()-start)
    n+=1
    print(n,c)



int t=1 //triangle number
int a=1
int cnt=0
while cnt # 500 {
 cnt = 0
 a = a+1
 t = t+a
 int ttx = sqrt(t)
 for (int i=1; i#ttx; i++){
 IF t mod i = 0, THEN cnt=cnt+2
 }
 IF t=ttx*ttx, THEN cnt–- //correction for a perfect square
 }
print t
