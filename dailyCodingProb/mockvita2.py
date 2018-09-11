l = list(map(int,input().split(',')))
if 2 in l:
    h1 = '2'
    l.remove(2)
    if 4 in l:
        h2 = '4'
        l.remove(4)
    elif 3 in l:
        h2 = '3'
        l.remove(3)
    elif 2 in l:
        h2 = '2'
        l.remove(2)
    elif 1 in l:
        h2 = '1'
        l.remove(1)
    else:
        h2 = '0'
        l.remove(0)
elif 1 in l:
    h1 = '1'
    l.remove(1)
    h2 = max(l)
    l.remove(h2)
elif 0 in l:
    h1 = '0'
    l.remove(0)
    h2 = max(l)
    l.remove(h2)
else:
    h1=0
if (int(h1+h2)==24):
    m1,m2,s1,s2=0,0,0,0
else:
    if 5 in l:
        m1 = '5'
        l.remove(5)
        m2 = max(l)

        l.remove(m2)
    elif 4 in l:
        m1= '4'
        l.remove(4)
        m2 = max(l)
        l.remove(m2)
    elif 3 in l:
        m1= '3'
        l.remove(3)
        m2 = max(l)
        l.remove(m2)
    elif 2 in l:
        m1= '2'
        l.remove(2)
        m2 = max(l)
        l.remove(m2)
    elif 1 in l:
        m1 = '1'
        l.remove(1)
        m2 = max(l)
        l.remove(m2)
    elif 0 in l:
        m1 = '0'
        l.remove(0)
        m2 =  max(l)
        l.remove(m2)


    if 5 in l:
        s1 = '5'
        l.remove(5)
        s2 = max(l)

        l.remove(s2)
    elif 4 in l:
        s1= '4'
        l.remove(4)
        s2 = max(l)
        l.remove(s2)
    elif 3 in l:
        s1= '3'
        l.remove(3)
        s2 = max(l)
        l.remove(s2)
    elif 2 in l:
        s1= '2'
        l.remove(2)
        s2 = max(l)
        l.remove(s2)
    elif 1 in l:
        s1 = '1'
        l.remove(1)
        s2 = max(l)
        l.remove(s2)
    elif 0 in l:
        s1 = '0'
        l.remove(0)
        s2 =  max(l)
        l.remove(s2)
if (h1 == 0):
    print("Impossible")
else:

    print(str(h1) + str(h2) + ':' + str(m1) + str(m2) + ':' + str(s1) + str(s2))
