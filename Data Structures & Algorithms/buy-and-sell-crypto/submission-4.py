class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        i = 0
        for j in range(1,len(prices)):
            profit = prices[j]-prices[i]
            if profit > 0 :
                maxprofit = max(profit,maxprofit)
            else:
                i = j 
        return maxprofit 