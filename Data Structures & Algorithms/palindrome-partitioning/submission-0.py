class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        strlen  = len(s)
        def dfs (index):
            if(index>=strlen):
                result.append(path.copy())
                return
            for i in range(index,strlen):
                if(self.isPalindrome(s,index,i)):
                    path.append(s[index:i+1]) 
                    dfs(i+1)
                    path.pop()   
        dfs(0)
        return result            

    def  isPalindrome(self,s,l,r):
        while(l<=r):
            if(s[l]!=s[r]):
                return False
            l = l+1
            r=r-1
        return True           