class Solution:
    def __init__(self):
        self.res = []
    def helper(self,input,result,count,level):
        if level == len(input):
            self.res.append(result[:])

        else:
            for i in range(len(input)):
                if count[i]==0:
                    continue
                else:
                    result[level] = input[i]
                    count[i]-=1
                    self.helper(input,result,count,level+1)
                    count[i]+=1


    def permute(self, nums):
        count = [1 for i in nums]
        result = [0 for i in nums]
        self.helper(nums,result,count,0)
        return self.res

print(Solution().permute([1,2,3]))
