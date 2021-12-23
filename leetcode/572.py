# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        
        while queue:
            curr = queue.popleft()
            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
        return False
    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)

'''
Runtime: 144 ms, faster than 78.59% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 14.8 MB, less than 92.98% of Python3 online submissions for Subtree of Another Tree.
'''