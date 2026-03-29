class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        visited = [False]*len(nums)
        def dfs ():
            if len(perm) == len(nums):
                res.append(perm.copy())
            for i in range(len(nums)):
                if not visited[i]:
                    perm.append(nums[i])
                    visited[i]=True
                    dfs()
                    perm.pop()
                    visited[i]=False
        dfs()
        return res