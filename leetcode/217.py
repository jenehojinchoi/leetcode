# 217. Contains Duplicate

# Approach 1. Comparing length
# # TC: O(n), SC: O(1) 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Approach 2. Hash Table
# TC: O(n), SC: O(n)
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        for i in hash:
            if hash[i] >= 2: 
                return True
        return False

