"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # graph = { 1: [2], 2: [1,3], 3: [2] }
        if not node:
            return None
        # old node -> new node
        old_to_new = {}
        visited = set()
        from collections import deque
        queue = deque()
        queue.append(node)
        visited.add(node)
        old_to_new[node] = Node(val=node.val)
        
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
                    old_to_new[nei] = Node(val=nei.val)
        
        for oldNode, newNode in old_to_new.items():
            for nei in oldNode.neighbors:
                
                newNode.neighbors.append(old_to_new[nei])
        return old_to_new[node]
