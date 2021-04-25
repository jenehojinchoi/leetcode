# 350. Intersection of Two Arrays II

# Approach 1. Using Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=collections.Counter(nums1)
        count2=collections.Counter(nums2)
        return sum([[num] * min(count1[num], count2[num]) for num in count1&count2], [])

# Approach 2. Using Counter II
class Solution(object):
    def intersect(self, nums1, nums2):
        count = collections.Counter(nums1)
        res = []
        for num in nums2:
            if count[num] > 0:
                res += num,
                count[num] -= 1
        return res

