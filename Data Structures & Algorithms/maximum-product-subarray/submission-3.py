class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax = 1,1
        for n in nums:
            tmp = n*curMax
            curMax = max(n*curMin,n*curMax,n)
            curMin = min(n*curMin,tmp,n)
            
            res = max(res,curMax)
        return res
