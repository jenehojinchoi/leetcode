# 152. Maximum Product Subarray

# Approach 1.
class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A + B)

# Approach 2.
class Solution:
    def maxProduct(self, nums):
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans