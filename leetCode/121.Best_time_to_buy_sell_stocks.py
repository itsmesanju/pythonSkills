#Iterate each item and find:
#
#
#minBuyPrice
#maxProfit
#
#As we want to identify the minBuyPrice, we will initiatlize it with infinite number so that we can get the min out of it and start comparing with each element.
#
#compare each element with the minBuyPrice and uppdate if it you find the minimum.
#
#For profit, compare if current prices are higher and update the variable.



class Solution(object):
    def maxProfit(self, prices):

        minBuyPrice = float('inf') # set initial low price to be infinite 
        maxProfit = 0 # set profit to be 0 
        for price in prices:
            if price < minBuyPrice:  # detect current price are lower than low
                minBuyPrice = price 
            else:  # detect current price are higher
                maxProfit = max(price-minBuyPrice, maxProfit) # compare the current difference and previous max profit
        return maxProfit
