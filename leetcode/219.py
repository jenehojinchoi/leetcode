# 219. Contains Duplicate II

# Approach 1.
# TC: O(n), SC: O(n)
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = defaultdict(list)
        for i in range(len(nums)):
            hash[nums[i]].append(i)
        for num in hash:
            if len(hash[num]) > 1:
                hash[num] = [abs(j-i) <= k for i, j in zip(hash[num][:-1], hash[num][1:])]
                if True in hash[num]:
                    return True
        return False
    
# Approach 2. 
# TC: O(n), SC: O(n)
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hash:
                if abs(i - hash[nums[i]]) <= k:
                    return True
                else:
                    hash[nums[i]] = i
            else:
                hash[nums[i]] = i
        return False
    
# Approach 3. 
# TC: O(n), SC: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False