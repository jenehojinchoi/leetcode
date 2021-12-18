# 207. Course Schedule

# Approach 1. BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for (curr, pre) in prerequisites:
            adj[pre].append(curr)
            degree[curr] += 1
            
        queue = collections.deque([])
        for v in range(numCourses):
            if degree[v] == 0:
                queue.append(v)
                
        visited = 0
        
        while queue:
            curr = queue.popleft()
            visited += 1
            
            for dep in adj[curr]:
                degree[dep] -= 1
                if not degree[dep]:
                    queue.append(dep)

        return visited == numCourses