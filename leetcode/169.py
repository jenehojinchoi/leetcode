# 169. Majority Element

# Didn't do Brute Force due to its bad time complexity
# Approach 1. Hash table
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)
        for i in nums:
            hashtable[i] += 1
        for i in hashtable:
            if hashtable[i] > len(nums)/2:
                return i

# Approach 2. Hash map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Approach 3. Sorting
# Time Complexity: O(n*logn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
# Approach 4. Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate