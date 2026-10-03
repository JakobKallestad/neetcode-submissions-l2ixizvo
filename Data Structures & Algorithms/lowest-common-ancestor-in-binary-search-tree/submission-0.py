# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def find_target(node, p, q):
            if p.val < q.val < node.val:
                return find_target(node.left, p, q)
            elif node.val < p.val < q.val:
                return find_target(node.right, p, q)
            else:  # split
                return node
            

        if p.val < q.val:
            return find_target(root, p, q)
        else:
            return find_target(root, q, p)
