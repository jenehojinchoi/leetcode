# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1
'''
Runtime: 36 ms, faster than 92.09% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16 MB, less than 72.36% of Python3 online submissions for Maximum Depth of Binary Tree.
'''