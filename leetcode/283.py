# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1