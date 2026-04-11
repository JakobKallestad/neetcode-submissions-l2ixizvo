class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.leftmost = Node(0, 0)
        self.rightmost = Node(0, 0)
        self.leftmost.right, self.rightmost.left = self.rightmost, self.leftmost

    def remove(self, node):
        left, right = node.left, node.right
        left.right = right
        right.left = left
    
    def insert(self, node):
        left, right = self.rightmost.left, self.rightmost
        left.right = node
        right.left = node
        node.left = left
        node.right = right


    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.insert(self.map[key])

        if len(self.map) > self.capacity:
            lru = self.leftmost.right
            self.remove(lru)
            del self.map[lru.key]
