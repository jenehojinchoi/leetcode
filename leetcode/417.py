# 417. Pacific Atlantic Water Flow

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()
        ans = []
        
        def dfs(i, j, array, prev_height):
            if (i < 0 or i == m or j < 0 or j == n or (i,j) in array or heights[i][j] < prev_height): 
                return
            array.add((i,j))
            
            dfs(i-1, j, array, heights[i][j])
            dfs(i+1, j, array, heights[i][j])
            dfs(i, j-1, array, heights[i][j])
            dfs(i, j+1, array, heights[i][j])
            
        for row in range(m):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, n-1, atl, heights[row][n-1])
                
        for col in range(n):
            dfs(0, col, pac, heights[0][col])
            dfs(m-1, col, atl, heights[m-1][col])
            
        for (i,j) in pac:
            if (i,j) in atl:
                ans.append([i,j])
        return ans


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        visited = [0]*(m*n)
        ans = []
        
        def dfs(i, j, add, prev_height):
            if (i < 0 or i == m or j < 0 or j == n):
                return 
            
            curr = i*n+j
            
            if (visited[curr] == 3 or visited[curr] == add or heights[i][j] < prev_height): 
                return
            
            visited[curr] += add
            if visited[curr] == 3:
                ans.append([i,j])
            
            dfs(i-1, j, add, heights[i][j])
            dfs(i+1, j, add, heights[i][j])
            dfs(i, j-1, add, heights[i][j])
            dfs(i, j+1, add, heights[i][j])
        
        for row in range(m):
            dfs(row, 0, 1, heights[row][0])
            dfs(row, n-1, 2, heights[row][n-1])
                
        for col in range(n):
            dfs(0, col, 1, heights[0][col])
            dfs(m-1, col, 2, heights[m-1][col])
            
        return ans