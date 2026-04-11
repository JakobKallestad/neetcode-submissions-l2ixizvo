# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = ListNode()
        l3 = prev_node
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            c = a + b + carry
            if c >= 10:
                carry = 1
                c = c - 10
            else:
                carry = 0
            
            cur_node = ListNode(c)
            prev_node.next = cur_node
            prev_node = prev_node.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return l3.next