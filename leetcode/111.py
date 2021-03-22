# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1. DFS w/ recursion
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#              return 0
#         if not root.left and not root.right:
#             return 1
#         if not root.left:
#             return self.minDepth(root.right) + 1
#         if not root.right:
#             return self.minDepth(root.left) + 1
#         return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
    

# Approach 2. BFS
class Solution:
    def minDepth(self, root:TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((root,1))
        while q:
            node, depth = q.popleft()

            if not node.left and not node.right:
                return depth
           
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

            