from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # jump x up one level
                x = parent[x]
            return x
        
        def union(a, b):
            nonlocal components
            ra = find(a)
            rb = find(b)
            if ra != rb:
                if size[ra] < size[rb]:
                    parent[ra] = rb
                    size[rb] += size[ra]
                else:
                    parent[rb] = ra
                    size[ra] += size[rb]
                components -= 1
        
        for a, b in edges:
            union(a, b)
        
        return components