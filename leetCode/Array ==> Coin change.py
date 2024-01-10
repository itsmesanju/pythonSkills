class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #In this implementation, dp[i] represents the minimum number of coins needed to make the amount i. 
        #The outer loop iterates through each coin denomination, and the inner loop updates the dp array for
        # each amount starting from the coin value. The final result is stored in dp[amount]. 
        
        #If dp[amount] is still set to float('inf'), it means that no valid combination exists, and 
        #we return -1. Otherwise, we return the minimum number of coins needed to make the given amount.

        # Create an array to store the minimum number of coins needed for each amount.
        #The index will indicate the coin.
        dp = [float('inf')] * (amount + 1)
        
        # The minimum number of coins needed to make amount 0 is 0
        dp[0] = 0
        
        # Iterate through each coin denomination
        for coin in coins:
            print(f"For coint: {coin}")
            # Update dp array for each amount starting from the coin value
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])    

        if dp[amount] != float('inf'):
            print(f"Result is {dp[amount]}")
            return dp[amount]
        else:
            return -1
