# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path_sum = [-float('inf')]
        
        def dfs(node):
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            parent_max_root = max( node.val + left_max + right_max, node.val, node.val + right_max, node.val + left_max)  # 4 cases --> all, exclude_both, exclude_left, exclude_right
            parent_max = max(node.val, node.val + right_max, node.val + left_max)  # 3 cases --> exclude_both, exclude_left, exclude_right
            max_path_sum[0] = max(max_path_sum[0], parent_max_root)
            return parent_max

        dfs(root)
        return max_path_sum[0]