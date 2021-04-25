# 349. Intersection of Two Arrays

# Approach 1. 
# TC: O(n), SC: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        if len(set1) >= len(set2):
            for cand in set2:
                if cand in set1:
                    res.append(cand)
            return res
        else:
            for cand in set1:
                if cand in set2:
                    res.append(cand)
            return res

# Approach 2. 
# TC: O(n), SC: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = collections.defaultdict(int)
        for i in nums2:
            if i in nums1:
                hash[i] = 1
        return hash.keys()