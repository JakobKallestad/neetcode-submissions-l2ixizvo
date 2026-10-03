from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        inorder_index = {val: i for i, val in enumerate(inorder)}
        preorder_i = 0

        def dfs(left, right):
            nonlocal preorder_i

            if left > right:
                return None

            # Preorder tells us the next root
            root_val = preorder[preorder_i]
            preorder_i += 1

            root = TreeNode(root_val)

            # Inorder tells us where left/right subtrees split
            mid = inorder_index[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)