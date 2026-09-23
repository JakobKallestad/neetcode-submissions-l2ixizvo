# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(c_node, c_sum):
            if not c_node:
                return False

            c_sum += c_node.val

            # leafnode:
            if not c_node.left and not c_node.right and c_sum == targetSum:
                return True

            return dfs(c_node.left, c_sum) or dfs(c_node.right, c_sum)

        return dfs(root, 0)