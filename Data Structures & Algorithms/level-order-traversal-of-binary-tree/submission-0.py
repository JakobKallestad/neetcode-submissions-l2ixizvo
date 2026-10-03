# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output = []

        # bfs
        while queue:
            level_output = []
            for i in range(len(queue)):
                e = queue.pop()
                level_output.append(e.val)
                if e.left:
                    queue.appendleft(e.left)
                if e.right:
                    queue.appendleft(e.right)
            output.append(level_output)
        return output

