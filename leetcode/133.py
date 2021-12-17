# 133. Clone Graph

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Approach 1. DFS Iterative
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        
        m = { node: Node(node.val) }
        stack = [node]
        
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in m:
                    stack.append(neighbor)
                    m[neighbor] = Node(neighbor.val)
                m[n].neighbors.append(m[neighbor])

        return m[node]

# Approach 2. BFS 
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        
        m = { node: Node(node.val) }
        deque = collections.deque([node])
        
        while deque:
            n = deque.popleft()
            for neighbor in n.neighbors:
                if neighbor not in m:
                    deque.append(neighbor)
                    m[neighbor] = Node(neighbor.val)
                m[n].neighbors.append(m[neighbor])

        return m[node]

'''
Runtime: 44 ms, faster than 44.69% of Python online submissions for Clone Graph.
Memory Usage: 13.8 MB, less than 63.35% of Python online submissions for Clone Graph.
'''

## Why use hashmap (dict)? : Faster to access neighbors of node
# Store node as a key and its neighbors as values
## Why is Approach 2 faster than Approach 1? : Uses deque. Faster in accessing and popping elements than just an array