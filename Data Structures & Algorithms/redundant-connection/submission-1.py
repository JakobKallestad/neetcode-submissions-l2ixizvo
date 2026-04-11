class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            nonlocal parent
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # jump x up one level
                x = parent[x]
            return x
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                parent[ra] = rb
                size[rb] += size[ra]
            else:
                parent[rb] = ra
                size[ra] += size[rb]
            return True
        
        for a, b in edges:
            if not union(a-1, b-1):
                return [a, b]
