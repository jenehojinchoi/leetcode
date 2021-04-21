# 226. Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1. 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left  = right
        return root

# Approach 2.
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            curr = q.popleft()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root