# 105. Construct Binary Tree from Preorder and Inorder Traversal


# Approach 1. 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])

            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

# keypoints
# the reason why we're doing line 5 (if inorder): 
# if inorder is None, it means it is leaf (has no children)

'''
Runtime: 148 ms, faster than 50.05% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.8 MB, less than 56.60% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''

# Approach 1 is very intuitive, easy to understand
# but it is slow since we're doing .index() on line 8, which is already O(n)


# Approach 2.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # to avoid finding index everytime, we build hash table
        val_index_dict = { num:idx for idx, num in enumerate(inorder) }
        self.root_index = 0
        
        def helper(left, right):
            
            if left > right:
                # Base case:
                # return None as empty Node
                return None
            
            else:
                root = TreeNode( preorder[self.root_index] )
                # update root index
                self.root_index += 1
            
                mid = val_index_dict[root.val]
                root.left = helper(left, mid-1)
                root.right = helper(mid+1, right)
                
                return root

        return helper(left = 0 , right = len(inorder)-1)

'''
Runtime: 52 ms, faster than 94.90% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 18.9 MB, less than 69.24% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''