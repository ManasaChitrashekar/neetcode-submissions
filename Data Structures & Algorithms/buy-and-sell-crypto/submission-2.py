class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0 
        maxProfit = 0
        for end in range(1,len(prices)): 
            profit = prices[end]-prices[start]
            if(profit >0):
                maxProfit = max(maxProfit,profit)
            else:
                start= end     
        return maxProfit