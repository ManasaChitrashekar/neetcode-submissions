class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={}
        def dfs(i,csum):
            if (i,csum) in dp:
                return dp[(i,csum)]
            if i == len(nums):
                return 1 if csum==target else 0
            dp[(i,csum)] = dfs(i+1,csum+nums[i])+dfs(i+1,csum-nums[i])
            return dp[(i,csum)]
        return dfs(0,0)