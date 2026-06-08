class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 ==1 :
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            temp = set(dp)
            for t in dp :
                if t+nums[i]==target:
                    return True
                temp.add(t+nums[i])
            dp = temp
        return True if target in dp else False