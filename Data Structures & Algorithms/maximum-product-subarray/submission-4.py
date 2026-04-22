class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax = 1,1
        for n in nums:
            tmp = n*curMax
            curMin, curMax = min(n*curMin,n*curMax,n),max(n*curMin,n*curMax,n)
            res = max(res,curMax)
        return res
