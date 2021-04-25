# 258. Add Digits

# Approach 1. loops
# TC: O(n^2)
class Solution:
    def helper(self, num):
        result = 0
        while num:
            result += num % 10
            num = num // 10
        return result
    
    def addDigits(self, num: int) -> int:
        while True:
            result = self.helper(num)
            if result >= 10:
                num = result
            else:
                return result
