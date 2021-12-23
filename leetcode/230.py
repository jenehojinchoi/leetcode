# 230. Kth Smallest Element in a BST

# Approach 1. 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = collections.deque([root])
        values = []
        
        while queue:
            curr = queue.popleft()
            values.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        values.sort()
        return values[k-1]

'''
Runtime: 48 ms, faster than 80.79% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.3 MB, less than 17.14% of Python3 online submissions for Kth Smallest Element in a BST.
'''

# improvement can be made because of memory usage.
# maybe there is a way to solve this problem without constructing a list?

# Approach 2. Stack

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

'''
Runtime: 48 ms, faster than 80.79% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 84.75% of Python3 online submissions for Kth Smallest Element in a BST.
'''