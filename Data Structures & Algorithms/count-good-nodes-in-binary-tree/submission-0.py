# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0
            if root.val >= maxValue:
                res = 1
            else:
                res = 0
            if root.val > maxValue:
                maxValue = root.val
            leftGood = dfs(root.right, maxValue)
            rightGood = dfs(root.left, maxValue)
            return res + leftGood + rightGood
        if not root:
            return 0
        return dfs(root, root.val)