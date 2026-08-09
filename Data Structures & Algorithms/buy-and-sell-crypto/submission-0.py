class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price

            curr_profit = price - lowest_price

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit