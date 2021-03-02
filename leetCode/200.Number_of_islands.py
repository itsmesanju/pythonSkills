#Top level overview (func numIslands):

#Iterate through each element in the grid.
#At each element, if grid[i][j] == "1":
#Increase our count of the number of islands (num_islands)
#perform DFS starting at grid[i][j] to mark all the entire connected component as one island.
#DFS overview (func dfs):
#Given a grid and the starting row and column indices,
#
#Change the value at grid[r][c] to "0" to mark this element as visited.
#For each of its neighbor indices, if the neighbor is both within bounds of the grid and has a value of "1" (i.e. is part of the same island), peform dfs on that neighbor.
#Time complexity: O(M * N), M=number of rows and N=number of columns
#
#In numIslands we look at every element in grid once, so M * N
#In the worst case, a call of dfs from numIslands can look at every element if the whole grid is an island, so also M * N
#O(2M * N) = O(M * N)
#Space complexity: O(1)

#No additional space needed to store visited nodes since we update in-place
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(grid, i, j)
                    
        return num_islands
    
    def dfs(self, grid, r, c):
        grid[r][c] = "0"
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                self.dfs(grid, nr, nc)
