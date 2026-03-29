class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def dfs(i,op):
            if(i>=n):
                if(op not in result):
                    result.append(op.copy())
                return  
            op.append(nums[i])
            dfs(i+1,op)
            op.pop()
            dfs(i+1,op)       

        dfs(0,[])
        return result