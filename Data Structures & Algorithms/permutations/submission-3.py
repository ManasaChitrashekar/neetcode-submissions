class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = defaultdict(bool)
        def backtrack(nums):
            if len(subset)==len(nums):
                res.append(list(subset.copy()))
            for num in  nums:
                if not visited[num] :
                    subset.append(num)
                    visited[num]=True
                    backtrack(nums)
                    subset.pop()
                    visited[num]=False
        backtrack(nums)
        return res        
        