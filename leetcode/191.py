# 191. Number of 1 Bits

# Approach 1. bin
# Time complexity: O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Approach 2. Check 32 bits of the number
# Time complexity: O(1), Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_1s = 0
        ## Assume the input is of int32
        for i in range(32):  
            num_of_1s += (n & 1)
            n = n >> 1
        return num_of_1s

# Approach 3. 
# Time complexity: O(1), Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_1s = 0
        while n != 0:
            num_of_1s += 1
            n &= (n-1)
        return num_of_1s