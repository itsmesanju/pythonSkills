class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:

        """
        We are using dynamic programming solution for maximizing profit within a given budget. 
        
        It uses a 1D list dp to represent the maximum profit achievable for each budget value. 
        The nested loops iterate over items and budget values to fill in the dynamic programming table.

        The outer loop iterates over each item.
        profit is calculated as the difference between the future and present values for the current item.
        The inner loop iterates over the budget values in reverse order.
        For each budget value j, the maximum profit is updated using the formula dp[j] = max(dp[j], dp[j - present[i]] + profit).
        The final result is stored in dp[budget], representing the maximum profit achievable with the given budget.

        """
        n = len(present)
        dp = [0] * (budget + 1) 
        for i in range(n):
            profit = future[i] - present[i]
            for j in range(budget, present[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - present[i]] + profit)
        return dp[budget]
