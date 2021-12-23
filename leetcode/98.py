# 98. Validate Binary Search Tree

class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.isValidBST(root.left, left, min(right, root.val)) and self.isValidBST(root.right, max(root.val, left), right)

'''
Runtime: 44 ms, faster than 72.15% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 79.87% of Python3 online submissions for Validate Binary Search Tree.
'''