# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        if not root:
            return True
        
        queue = deque([(float("-inf"), root, float("inf"))])

        while queue:
            low, curr, high = queue.popleft()
            if  not (low < curr.val < high):
                return False
            if curr.left:
                queue.append([low,curr.left,curr.val])
            if curr.right:
                queue.append([curr.val,curr.right,high])
        return True
            

        