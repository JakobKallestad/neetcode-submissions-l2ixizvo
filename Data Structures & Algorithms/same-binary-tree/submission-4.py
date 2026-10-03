# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = deque([p])
        stack_q = deque([q])

        def check_equal_nodes(p_node, q_node):
            if not p_node and not q_node:
                return True
            if (p_node and not q_node) or (not p_node and q_node):
                return False
            if p_node.val != q_node.val:
                return False
            if p_node.left:
                if not q_node.left:
                    return False
                if p_node.left.val != q_node.left.val:
                    return False
            if p_node.right:
                if not q_node.right:
                    return False
                if p_node.right.val != q_node.right.val:
                    return False
            return True


        while stack_p and stack_q:
            p_node = stack_p.pop()
            q_node = stack_q.pop()
            if not check_equal_nodes(p_node, q_node):
                return False
            
            if p_node and p_node.left:
                stack_p.append(p_node.left)
            if p_node and p_node.right:
                stack_p.append(p_node.right)
            if q_node and q_node.left:
                stack_q.append(q_node.left)
            if q_node and q_node.right:
                stack_q.append(q_node.right)
        
        if stack_p or stack_q:
            return False
        return True