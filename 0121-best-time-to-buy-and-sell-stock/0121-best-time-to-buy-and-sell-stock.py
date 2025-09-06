class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can use min_price = float('inf') as a placeholder for anything
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        if max_profit <= 0:
            return 0
        return max_profit