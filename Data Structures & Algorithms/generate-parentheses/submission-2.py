class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_index,close_index,cur):
            if len(cur)==2*n:
                res.append(cur)
                return
            if open_index<n:
                dfs(open_index+1,close_index,cur+"(")
            if close_index< open_index:
                dfs(open_index,close_index+1,cur+")")
        dfs(0,0,"")
        return res