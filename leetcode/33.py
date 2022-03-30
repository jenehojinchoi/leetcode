# 33. Search in Rotated Sorted Array

# Approach 1. Simply finding index
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

# Approach 2. Binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = int((l+r)/2)
            
            if target == nums[m]:
                return m
            
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1