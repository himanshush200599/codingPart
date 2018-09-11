for _ in range(int(input())):
    s = input()
    flag = 0
    l = []
    for i in s:

        if i == '(' or i == '{' or i == '[':
            l.append(i)
        elif i  == ')' or i  == '}' or i  == ']':
            if  l != [] and l[-1]=='(':
                l.pop()
            else:
                flag = 1
                break
        
        if l==[] and len(s[s.index(i):])==0:
            break
    if flag ==0 and l==[]:
        print("balanced")
    else:
        print("not balanced")
