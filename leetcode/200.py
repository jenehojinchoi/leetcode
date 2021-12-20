# 200. Number of Islands

from collections import deque
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        queue = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.bfs(grid,queue)
                    count += 1
        return count
    
    
    def bfs(self,grid,queue):
        m = len(grid)
        n = len(grid[0])
        
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < m and 0 <= j < n and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0
