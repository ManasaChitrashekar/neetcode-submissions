class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] *n
        # for _ in range(m+1):
        #     dp.append([0]*(n+1))
        dp.append([1]*(n))
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j] = dp[j]+dp[j+1]
                #bottom is dp[j] itself and right is dp[j+1]

        return dp[0]
