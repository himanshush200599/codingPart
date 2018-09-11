for i in range(int(input())):
    n = int(input())
    while(1):
        n+=1
        n = str(n)
        if n.count('3')==3:
            print(n)
            break
        n = int(n)  
