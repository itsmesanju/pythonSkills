"""
Given are only two valid moves :
  Move right
  Move down
  
Hence, it is clear number of paths from cell (i,j) = sum of paths from cell( i+1,j) and cell(i,j+1) It becomes a DP problem.

BASE CASES
If we are in last row, i == m-1, we only have the choice to move RIGHT, Hence number of moves will be 1.
If we are in last column, j == n-1, we only have the choice to move DOWN, Hence number of moves will be 1.

Step-by-Step Solution:
Step 1: Initialize the DP Table

Create a 2D DP (dynamic programming) table of size m x n to store the number of unique paths for each cell.
Initialize the rightmost column and bottom row of the DP table to 1 because there's only one way to reach each cell in those rows/columns (by moving all the way right or all the way down).

Step 2: Fill in the DP Table

Start from the second-to-last row and second-to-last column (i.e., i = m - 2 and j = n - 2).
For each cell (i, j) in the grid:
Calculate the number of unique paths to reach (i, j) as the sum of the unique paths from the cell below (i+1, j) and the cell to the right (i, j+1). Use this formula: dp[i][j] = dp[i+1][j] + dp[i][j+1].
Continue filling in the DP table row by row and column by column until you reach the top-left corner (dp[0][0]).

Step 3: Return the Result

Return the value stored in the top-left corner of the DP table (dp[0][0]), which represents the number of unique paths from the top-left corner to the bottom-right corner.

Time Complexity (TC): O(m * n).
Space Complexity (SC): O(m + n).

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table filled with zeros
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the rightmost column and bottom row to 1
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        
        # Fill in the DP table bottom-up
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        # Return the result stored in the top-left corner
        return dp[0][0]
