class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0 
        maxsofar = 0
        jumps = 0 
        for i in range(len(nums)-1):
            maxsofar = max(maxsofar,i+nums[i])
            if i == cur:
                cur = maxsofar
                jumps +=1
        return jumps