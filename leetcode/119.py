# 119. Pascal's Triangle II

# Approach 1. Iteration
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        stack = []
        stack.append([])
        for i in range(0, rowIndex+1):
            before = stack.pop()
            after = []
            for j in range(i+1):
                if j == 0 or j == i: after.append(1)
                else: after.append(before[j-1] + before[j])
            stack.append(after)
        return stack.pop()
    
# Approach 2. Factorial
from math import factorial as f

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	result = []
    	for i in range(rowIndex+1):
    		result.append(round(f(rowIndex)/((f(i)*f(rowIndex-i)))))
    	return result

