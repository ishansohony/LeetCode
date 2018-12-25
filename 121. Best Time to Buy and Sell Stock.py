class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_profit = 0
        min_price = 999999
        for i in prices:
            min_price = min(i, min_price)
            max_profit = max(i - min_price, max_profit)
        
        return max_profit
        
