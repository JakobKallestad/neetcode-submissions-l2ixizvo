# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(c_node):
            if not c_node:
                return 0
            
            left_d = dfs(c_node.left)
            right_d = dfs(c_node.right)
            return max(left_d, right_d)+1

        return dfs(root)
        