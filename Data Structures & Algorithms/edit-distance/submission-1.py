class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        m,n = len(word1),len(word2)
        for _ in range(m+1):
            dp.append([float("inf")] * (n+1))
        p = m
        for i in range(m+1):
            dp[i][n]= p
            p -=1
        p= n
        for j in range(n+1):
            dp[m][j]=p
            p -=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]= dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        return dp[0][0]