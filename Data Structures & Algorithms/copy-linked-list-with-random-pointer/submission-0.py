"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict, deque

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head_copy = None
        node_map = defaultdict() # id(node) --> index
        all_nodes = []
        current = None

        while head:
            current = Node(head.val, head.next, head.random)
            node_map[id(head)] = len(all_nodes)
            all_nodes.append(current)
            if not head_copy:
                head_copy = current
            head = head.next
        
        print("FINAL")
        for i, n in enumerate(all_nodes):
            print("node", i)
            # fix next
            if i == len(all_nodes) -1:
                n.next = None
            else:
                n.next = all_nodes[i+1]
            
            # fix random
            if not n.random is None:
                j = node_map[id(n.random)]
                n.random = all_nodes[j] # finds the copy of the node to link to because both the copy and original would share the same index
        
        return head_copy



# I think i can do the following:
# 1) start with head and follow random until a loop is discovered or it ends in null. (or visits a previously copied node see point 6)
# 2) along the way add all the nodes to a stack.
# 3) pop off each node in the stack (reverse order). 
# 4) Create a copy of this node and set node.random to be the previous copy_node created from in the stack.
# 5) When reaching the original node then we have to not create a new copy_node, but instead
# Take the first copy_node we made when popping from the queue and set the node.random here to be the previous copy_node
# 6) If we ever run into a node doing this that has already been "copied" (use a hashmap with id(node)),
# Then we dont create a new copy_node, but instead use this one dirctly and stop following the node.random.
# 
# The self-looping thing is a bit annoying for my logic.

# I will look at the solution.
