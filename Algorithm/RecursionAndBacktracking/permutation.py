def permutation(input,result,count,level):
    if level == len(input):
        print(result)
    else:
        for i in range(len(input)):
            if count[i]==0:
                continue
            else:
                result[level] = input[i]
                count[i]-=1
                permutation(input,result,count,level+1)
                count[i]+=1
input = "abcdefghijk"
count = [1 for i in input]
result = [0 for i in input]
permutation(input,result,count,0)
