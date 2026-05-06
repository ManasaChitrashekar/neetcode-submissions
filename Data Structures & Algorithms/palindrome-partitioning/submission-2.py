class Solution:
    def partition(self, s: str) -> List[List[str]]:
        reslist = []
        def ispalindrone(l,r):
            while l< r :
                if s[l]!=s[r]:
                    return False
                l +=1
                r -=1
            return True
            
        def dfs(i,path):
            if i == len(s):
                reslist.append(path.copy())
                return 
            for j in range(i,len(s)):
                if not ispalindrone(i,j):
                    continue
                path.append(s[i:j+1])
                dfs(j+1,path)
                path.pop()
        dfs(0,[])
        return reslist
            