class Solution(object):
    def maxProfit(self, prices):

        low = float('inf') # set initial low price to be infinite 
        profit = 0 # set profit to be 0 
        for price in prices:
            if price < low:  # detect current price are lower than low
                low = price 
            else:  # detect current price are higher
                profit = max(price-low, profit) # compare the current difference and previous max profit
        return profit
