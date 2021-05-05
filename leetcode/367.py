# 367. Valid Perfect Square

# Approach 1. 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = str(num ** 0.5)
        return sqrt.endswith('.0')

# Approach 2. 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary Search (can we find a squre root of num)
        left, right = 0, num
        while left < right:
            middle = (left + right) // 2
            squre = middle * middle
            if squre == num:
                return True
            elif squre < num:
                left = middle + 1
            else:
                right = middle - 1
        return True if right ** 2 == num else False