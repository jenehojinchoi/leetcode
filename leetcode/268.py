# 268. Missing numbers

# Approach 1. 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length+1):
            if i not in nums:
                return i
        return None

# Approach 2. 
class Solution:
    def missingNumber(self, n: List[int]) -> int:
        return len(n)*(len(n)+1)//2 - sum(n)