# 136. Single Number

# Approach 1. count
# Time complexity: O(n^2), Space complexity: O(n)
class Solution: 
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

# Approach 2. sum
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

# Approach 3. hash table
# Time complexity: O(n), Space complexity: O(n)
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table: 
            if hash_table[i] == 1:
                return i

# Approach 4. bit manipulation
# Time complexity: O(n), Space complexity: O(1)
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a