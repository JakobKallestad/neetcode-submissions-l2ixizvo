# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        current = root
        while current:
            self.stack.append(current)
            current = current.left


    def next(self) -> int:
        n = self.stack.pop()
        current = n.right
        while current:
            self.stack.append(current)
            current = current.left
        return n.val

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()