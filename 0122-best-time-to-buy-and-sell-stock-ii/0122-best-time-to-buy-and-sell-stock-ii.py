class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        total_profit = []

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
            if max_profit != 0:
                total_profit.append(max_profit)
                max_profit = 0
                min_price = prices[prices.index(price)]

        Sum = sum(total_profit)

        return Sum