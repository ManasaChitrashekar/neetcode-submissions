class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = 1,1
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        for i in range(n):
            prefix[i]= pre
            pre = pre*nums[i]
       
        for i in range(n-1,-1,-1):
            postfix[i]=post
            post = post*nums[i]
       
        res = [0]*n
        for i in range(n):
           res[i]=prefix[i]* postfix[i]
        return res
      
       