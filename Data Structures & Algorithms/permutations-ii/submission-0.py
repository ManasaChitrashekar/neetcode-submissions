class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        path = []
        nums.sort()
        n=len(nums)
        def dfs():
            if len(path)==n:
                res.append(path.copy())
                return
            for i in range(n):
                if i in visited:
                    continue
                if i>0 and nums[i]==nums[i-1] and i-1 not in visited:
                    continue
                visited.add(i)
                path.append(nums[i])
                dfs()
                path.pop()
                visited.remove(i)

        dfs()
        return res