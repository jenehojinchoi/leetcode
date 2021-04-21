# 228. Summary Ranges

# Approach 1. 
# TC: O(n), SC: O(n)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        min, max = nums[0], float(inf)
        i = 0
        while i in range(len(nums)):
            min = nums[i]
            while i != len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
            max = nums[i]
            if max== min:
                result.append(str(min))
            else:
                result.append(str(min)+'->'+str(max))
            i += 1
        return result

# Approach 2. 
# TC: O(n), SC: O(n)
class Solution:
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

# Approach 3.
# TC: O(n), SC: O(n)
class Solution:    
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges.append(r)
            r[1:] = [n]
        return ['->'.join(map(str, r)) for r in ranges]