class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0 
        for i in range(0,len(nums)+1):
            sum = sum+i
        res = 0 
        for i in nums :
            res = res+i
        return sum-res