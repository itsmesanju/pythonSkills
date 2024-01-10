"""
We can solve this problem using a state machine approach. The three states we need to consider are:


For each day in the prices array, update the states based on the three possible actions: buy, sell, and cooldown.

Buy (update buy): You can either continue to hold the stock from the previous day or buy on the current day. Choose the maximum of the two.
Sell (update sell): You can either continue to hold no stock or sell on the current day. Choose the maximum of the profit from buying on the previous day plus the current day's price or the profit from selling on the previous day.
Cooldown (update cooldown): You can either continue to do nothing or cooldown on the current day. Choose the maximum of the profit from selling on the previous day or the profit from doing nothing on the previous day.

Final Answer:
The maximum profit is the maximum of the last day's sell and cooldown.

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
