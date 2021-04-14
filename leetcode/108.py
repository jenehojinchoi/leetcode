# 108. Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1. Recursion            
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            n = len(nums)
            if n == 1:
                return TreeNode(nums[0])
            elif n == 2:
                root = TreeNode(nums[0])  
                root.right = TreeNode(nums[1])
                return root
            else:
                mid = int(n/2)
                root = TreeNode(nums[mid])
                root.left = self.sortedArrayToBST(nums[:mid])
                root.right = self.sortedArrayToBST(nums[mid+1:])
                return root

# Same approach 1, Saving memory. No need to include when n==1, n==2 because it's going to be calculated anyways
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root