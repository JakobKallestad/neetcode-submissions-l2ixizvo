# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def bfs(root):
            queue = deque([(root, -float('inf'))])
            while queue:
                c_node, c_max = queue.popleft()
                if c_node.val >= c_max:
                    self.res += 1
                    c_max = c_node.val
                if c_node.left:
                    queue.append((c_node.left, c_max))
                if c_node.right:
                    queue.append((c_node.right, c_max))
        
        bfs(root)
        return self.res
        