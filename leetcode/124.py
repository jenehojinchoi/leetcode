# 124. Binary Tree Maximum Path Sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            res[0] = max(res[0], root.val + left + right)
            return root.val + max(left, right)
        
        res = [-float('inf')]
        helper(root)
        
        return res[0]

'''
Runtime: 88 ms, faster than 64.63% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 21.7 MB, less than 60.23% of Python3 online submissions for Binary Tree Maximum Path Sum.
'''