class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = nums[0] 
        for i in range(1,len(nums)):
            if cur < 0: cur = 0 
            cur +=nums[i]
            maxsum = max(cur,maxsum)
        return maxsum 