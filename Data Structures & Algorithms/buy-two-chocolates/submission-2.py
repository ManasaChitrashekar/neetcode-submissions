class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        moneypaid =prices[0]+prices[1]
        return money if moneypaid>money  else money-moneypaid