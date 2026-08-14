"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = dict()
        
        queue = collections.deque()

        visited = set()
        queue.append(node)
        visited.add(node)
        old_to_new[node] = Node(val=node.val)
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    old_to_new[nei] = Node(val=nei.val)
                    visited.add(nei)
                    queue.append(nei)
        
        for old,new in old_to_new.items():
            for nei in old.neighbors:
                new_item = old_to_new[nei]
                new.neighbors.append(new_item)

        return old_to_new[node]
        

        