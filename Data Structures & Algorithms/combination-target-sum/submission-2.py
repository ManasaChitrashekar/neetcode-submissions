class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i,sumc):
            if sumc >target or  i == len(nums):
                return

            if  sumc ==target:
                res.append(path.copy())
                return
                
            path.append(nums[i])
            dfs(i,sumc+nums[i])

            path.pop()
            dfs(i+1,sumc)

            return 
        dfs(0,0)
        return res
        
        