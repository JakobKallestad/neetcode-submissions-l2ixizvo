# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            rigth = dfs(node.right)
            values.append(node.val)

        
        dfs(root)

        values.sort()   # n log n --> could do n log k using a heap, but k can be as large as n for this problem.
        return values[k-1]