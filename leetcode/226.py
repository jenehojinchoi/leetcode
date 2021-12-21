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

'''
Runtime: 32 ms, faster than 68.69% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 47.45% of Python3 online submissions for Invert Binary Tree.
'''

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