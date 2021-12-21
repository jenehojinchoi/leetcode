# 102. Binary Tree Level Order Traversal 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        currLevel = [root]
        
        while currLevel:
            nextLevel = []
            temp = []
            
            for node in currLevel:
                temp.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel
            ans.append(temp)

        return ans

'''
Runtime: 32 ms, faster than 84.13% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.6 MB, less than 68.10% of Python3 online submissions for Binary Tree Level Order Traversal.
'''