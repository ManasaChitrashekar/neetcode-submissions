class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        m,n = len(s1),len(s2)
        dp = []
        for _ in range(m+1):
            dp.append([False]*(n+1))
        dp[m][n]=True
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                # track where is I 
                if i <m and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]= True
                elif j <n and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]  = True 
        return dp[0][0]