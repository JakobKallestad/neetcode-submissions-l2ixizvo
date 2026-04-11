# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        d1 = []
        d2 = []

        while l1:
            d1.append(l1.val)
            l1 = l1.next
        while l2:
            d2.append(l2.val)
            l2 = l2.next
        
        d1 = int(''.join(map(str, reversed(d1))))
        d2 = int(''.join(map(str, reversed(d2))))
        res = str(d1 + d2)

        right = None
        for r in res:
            c_node = ListNode(int(r), right)
            right = c_node
        return c_node