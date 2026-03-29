class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compmap ={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in compmap:
                return [compmap[diff],i]
            compmap[nums[i]]=i
        return [0,0]