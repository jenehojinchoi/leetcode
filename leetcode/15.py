# 15. Three Sum

# Approach 1. 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length, result = len(nums), []
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            l, r = i+1, length-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                l += 1
                r -= 1
        return result