class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        """
        this dynamic programming solution iteratively updates the dp array by considering both paid and free painters
        for each wall. The inner loop ensures that the time constraints are properly accounted for when using 
        the paid painter. The final result is the minimum cost to paint all the walls.

        Dynamic Programming Iteration:
        ==============================
        Use two nested loops:
        The outer loop (for i in range(n)) iterates over each wall.
        The inner loop (for j in range(n, 0, -1)) iterates backward from n to 1, representing the number of walls considered so far.
        Update dp Array:
        ================
        For each wall i and each value of j, update dp[j] based on two options:
        Paid Painter Option: dp[j] = min(dp[j], dp[max(j-1-time[i], 0)] + cost[i])
        This considers using the paid painter for the current wall. It updates the cost to paint j walls, taking into account the time constraint of the paid painter.
        Free Painter Option: dp[j] = min(dp[j], dp[j-1] + cost[i])
        This considers using the free painter for the current wall, and it updates the cost accordingly.

        """
        n = len(cost)
        
        # dp[i] represents the minimum cost to paint the first i walls
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(n):
            for j in range(n,0,-1):
                dp[j] = min(dp[j], dp[max(j-1-time[i],0)]+cost[i])
        
        return dp[n]
