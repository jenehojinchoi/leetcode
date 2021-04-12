# 172. Factorial Trailing Zeroes
# Counting how many 5s are in n is important 

# Approach 1. Iteration
# Time Complexity: O(logn)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 5
        result = 0
        while x <= n:
            result += n//x
            x *= 5
        return result

# Approach 2. One liner
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else int(n/5 + self.trailingZeroes(n/5))