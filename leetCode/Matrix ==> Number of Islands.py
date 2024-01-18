class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        I used a main function (numIslands) and a recursive one (mark_island).
In the main function I iterate through all elements of the 2D array and if an element is "1" it means it is land. 
Therefore I use the mark_island recursive function to check for all the other pieces of land (adjacent neighbours and recursively, the adjacent neighbours of the initial neighbours) from this same island. 

I marked all the visited pieces of land by changing their value to "2". Returning to the main for loop, we mark an additional island everytime we find a new "1" in the main for loop, as in the worst case scenario it represents an island by itself.
        """

    def mark_island(self, grid: List[List[str]], i: int, j: int):

        #Check out of bounds
        n=len(grid)
        m=len(grid[0])

        if i<0 or i>=n or j<0 or j>=m:
            return

        if grid[i][j] == "1":
            grid[i][j] = "2"
            #Left
            self.mark_island(grid, i, j-1)
            #Right
            self.mark_island(grid, i, j+1)
            #Up
            self.mark_island(grid, i-1, j)
            #Down
            self.mark_island(grid, i+1, j)
        else:
            return

    def numIslands(self, grid: List[List[str]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        nr_islands=0

        if n ==0:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    nr_islands+=1
                    self.mark_island(grid,i,j)
        
        return nr_islands
                

                
