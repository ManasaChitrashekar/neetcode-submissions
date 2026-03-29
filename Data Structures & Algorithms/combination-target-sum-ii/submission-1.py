class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index,op,sum):
            if(sum == target and op not in res):
                res.append(op.copy())
                return
            if sum > target or index == len(candidates):
                return    
            op.append(candidates[index])
            dfs(index+1,op,sum+candidates[index]) 
            op.pop()
            dfs(index+1,op,sum) 
        dfs(0,[],0)
        return res          