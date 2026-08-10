# Find the maximum profit by buying low and selling later at the highest price.

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit