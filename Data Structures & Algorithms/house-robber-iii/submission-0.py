# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # observation --> backtracking.
        
        def dfs(c_node):
            
            if not c_node:
                return 0, 0

            # left
            left_leave, left_steal = dfs(c_node.left)
            
            # righ
            right_leave, right_steal = dfs(c_node.right)

            # at a node - on the way back:
            print(left_steal+right_steal, left_leave+right_leave+c_node.val)
            return max(left_steal, left_leave)+max(right_steal, right_leave), left_leave+right_leave+c_node.val
            
        
        a, b = dfs(root)
        return max(a, b)