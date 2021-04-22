# 231. Power of Two

# Approach 1. Loop
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            n = n / 2
            if n % 2 != 0 and n != 1:
                return False
        return True

# Approach 2. Bit manipulation 
class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        if x == 0:
            return False
        return (x & (x - 1)) == 0