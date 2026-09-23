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

            n_sum = c_sum + c_node.val
            # go left
            a = dfs(c_node.left, n_sum)


            # go right
            b = dfs(c_node.right, n_sum)

            # leafnode:
            if not c_node.left and not c_node.right and n_sum == targetSum:
                return True

            return a or b



        
        return dfs(root, 0)