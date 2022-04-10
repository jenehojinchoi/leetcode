# 347. Top K Frequent Elements

# Approach 1. Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = collections.Counter(nums)
        hash_set = sorted(hash_set.items(), key=lambda x:x[1], reverse=True)
        return [i[0] for i in hash_set[:k]]

'''
Runtime: 139 ms, faster than 53.04% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.8 MB, less than 24.62% of Python3 online submissions for Top K Frequent Elements.
'''

# Approach 2. Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        if k == len(nums):
            return nums
        # O(N) time
        count = collections.Counter(nums)   
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 