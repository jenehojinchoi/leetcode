# 257. Binary Tree Paths

# Approach 1. DFS w/ recursion
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: 
            return []
        if not root.left and not root.right: return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.left)]\
            +[str(root.val) + '->' + i for i in self.rootToLeafPaths(root.right)]

# Approach 2. BFS Iterative w/ Stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        paths = []
        stack = [(root, [])]
        
        while stack:
            node, path = stack.pop()
            path = path + [str(node.val)]
            if not node.left and not node.right:
                paths.append(
                    '->'.join(path)
                )
            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        
        return paths