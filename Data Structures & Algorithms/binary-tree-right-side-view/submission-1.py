# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.visible_map = {}

        def dfs(node, depth):
            if not node:
                return
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            self.visible_map[depth] = node.val

        dfs(root, 0)
        return [v for k,v in sorted(self.visible_map.items(), key=lambda x: x[0])]
        