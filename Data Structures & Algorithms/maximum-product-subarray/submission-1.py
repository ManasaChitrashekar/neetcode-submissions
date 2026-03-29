class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax = 1,1
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue
            else:
                tmp = n*curMax
                curMax = max(curMax*n,curMin*n,n)
                curMin = min(tmp,curMin*n,n)
                res = max(res,curMax)
        return res
