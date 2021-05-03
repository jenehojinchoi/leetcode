# 278. First Bad Version

# Approach 1. Time Limit Exceeded
class Solution:
    def firstBadVersion(self, n):
        for i in range(n):
            if isBadVersion(i):
                return i
        return null
        
# Approach 2. Binary Search
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = int(left+ (right-left)/2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
        
# Approach 3. Using library
import bisect
class Solution():
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)