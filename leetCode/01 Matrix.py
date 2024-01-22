"""
The approach involves using Breadth-First Search (BFS) to traverse the matrix starting from each '0' cell. 

We initialize a result matrix with maximum distances, enqueue '0' cells with distance 0, 
and perform BFS to update distances in the result matrix. 

The result matrix contains the distances to the nearest '0' for each cell.

"""
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        ans = [[float('inf')] * N for i in range(0, M)]

        queue = deque()
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    ans[i][j] = 0
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while queue:
            x, y, distance = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and ans[nx][ny] > distance + 1:
                    ans[nx][ny] = distance + 1
                    queue.append((nx, ny, distance + 1))
        
        return ans
