class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prod = 1
        pre = [0]*len(nums)
        for i in range(len(nums)):
            pre[i]=prod
            prod = prod* nums[i]
        prod = 1
        post = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            post[i]=prod
            prod = prod*nums[i]
        for i in range(len(nums)):
            res[i]= pre[i]*post[i]  
        return res      