class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        path= []
        n = len(nums)
        def backtrack():
            if len(path)==n:
                res.append(path.copy())
                return
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    visited.remove(i)
        backtrack()
        return res

