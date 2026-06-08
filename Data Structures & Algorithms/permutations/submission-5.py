class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]*len(nums)
        path = []
        res = []
        def backtrack():
            if len(path)==len(nums):
                res.append(path.copy())
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True 
                    backtrack()
                    path.pop()
                    visited[i] = False
        backtrack()
        return res