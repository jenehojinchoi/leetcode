# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My approach, but bad time complexity
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        
        if abs(ldepth - rdepth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

# Another approach, but bad space complexity
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return (0, True)
            lheight, lbalanced = helper(root.left)
            rheight, rbalanced = helper(root.right)
            
            return (max(lheight, rheight) + 1, lbalanced and rbalanced and abs(lheight-rheight) <= 1)
        return helper(root)[1]