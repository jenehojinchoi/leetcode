# 200. Number of Islands

# Approach 1. BFS
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
                    grid[i][j] = '#'
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
                    grid[i][j] = '#'


# Approach 2. DFS
class Solution:
    def check(self, grid, i, j):
        # 내가 0 혹은 visited 거나 주변이 다 wall일때
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        # 내가 1일때
        grid[i][j] = '#'
        self.check(grid, i+1, j)
        self.check(grid, i, j+1)
        self.check(grid, i-1, j)
        self.check(grid, i, j-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.check(grid, i, j)
                    count += 1
        return count