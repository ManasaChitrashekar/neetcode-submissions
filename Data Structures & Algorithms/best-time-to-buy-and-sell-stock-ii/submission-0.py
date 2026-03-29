class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        i = 0 
        while i < len(prices):
            if i+1<len(prices) and prices[i]<prices[i+1]:
                res += prices[i+1]-prices[i]
            i +=1
        return res