class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cash = 0
        hold = float('-inf')

        """
        The algorithm is designed for optimizing stock trading with transaction fees. 
        
        It iterates through the array of stock prices, updating two variables (cash and hold) at each step. 
        The goal is to maximize profit, considering buying and selling stocks with a transaction fee. 
        
        The key steps involve calculating the maximum profit when not holding any stock (cash) and when holding a stock (hold).
        The algorithm employs dynamic programming principles to iteratively update these values based on the current stock price and previous states. Ultimately, the algorithm returns the maximum profit achievable.
        """
        
        for i in range(n):
            prev_cash = cash
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, prev_cash - prices[i])

        return cash
