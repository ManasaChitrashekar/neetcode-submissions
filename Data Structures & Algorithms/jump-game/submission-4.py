class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i            # shrink goalpost
            # no else — just keep going
        return goal == 0            # ✅ did goalpost shrink all the way to start?