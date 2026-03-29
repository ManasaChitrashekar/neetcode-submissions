class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        i =0
        sum = 0
        for j in range(len(nums)):
            sum = sum+nums[j]
            while sum>=target:
                minlen = min(minlen,j-i+1)
                sum = sum-nums[i]
                i+=1
        return minlen if minlen!=float('inf') else 0