class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_c,close_c,cur):
            if len(cur)==2*n:
                res.append(cur)
                return
            if open_c < n :
                dfs(open_c+1,close_c,cur+'(')
            if close_c < open_c :
                dfs(open_c,close_c+1,cur+')')
        dfs(0,0,"")
        return res