# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        def dfs_inner(node, sub_node):
            if not node and not sub_node:
                return True
            if not node or not sub_node:
                return False
            
            if node.val != sub_node.val:
                return False
            
            left = dfs_inner(node.left, sub_node.left)
            right = dfs_inner(node.right, sub_node.right)
            return left and right
            
            

        def dfs_outer(node, subRoot):
            if not node:
                return False
            if dfs_inner(node, subRoot):
                return True
            left = dfs_outer(node.left, subRoot)
            right = dfs_outer(node.right, subRoot)
            return left or right

        return dfs_outer(root, subRoot)