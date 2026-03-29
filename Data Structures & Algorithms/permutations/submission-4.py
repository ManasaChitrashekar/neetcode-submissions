class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        visited = [False]*len(nums)

        def backtrack():
            if len(sub)==len(nums):
                res.append(sub.copy())
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    sub.append(nums[i])
                    visited[i]= True 
                    backtrack()
                    sub.pop()
                    visited[i]=False 
        backtrack()
        return res 