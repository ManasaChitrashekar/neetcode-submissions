class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        i = 0
        for step in nums:
            if maxreach<i :
                return False
            maxreach = max(maxreach,i+step)
            i+=1
        return True