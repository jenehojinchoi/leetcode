# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        lo = 0
        hi = len(nums)-1
        while nums[lo] > nums[hi]:
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]:
                # notice it's not mid-1
                hi = mid
            else:
                lo = mid+1
        return nums[lo]   

'''
Runtime: 36 ms, faster than 91.27% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.5 MB, less than 61.29% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
'''