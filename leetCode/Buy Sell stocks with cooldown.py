"""
We can solve this problem using a state machine approach. The three states we need to consider are:

buy: The maximum profit when buying a stock on the current day.
sell: The maximum profit when selling a stock on the current day.
cooldown: The maximum profit when doing nothing (cooldown) on the current day.

In this approach, we iterate through the prices array and update the buy, sell, and cooldown variables accordingly. The key is to maintain the state transitions based on the actions of buying, selling, and cooling down, and at the end, return the maximum of the last day's sell and cooldown.

Here's a Python implementation without dynamic programming:
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        buy, sell, cooldown = float('-inf'), 0, 0

        for price in prices:
            prev_buy = buy
            buy = max(cooldown - price, buy)
            cooldown = sell
            sell = max(prev_buy + price, sell)

        # The maximum profit is the maximum of the last day's sell and cooldown
        return max(sell, cooldown)
