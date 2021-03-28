# 118. Pascal's Triangle

# Approach 1. Iteration
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        parent = []
        for i in range(numRows):
            parent.append([])
            if i==0:
                parent[i].append(1)
            elif i==1:
                parent[i].append(1)
                parent[i].append(1)
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        parent[i].append(1)
                    else:
                        parent[i].append(parent[i-1][j-1] + parent[i-1][j])
        return parent

# Approach 2. 