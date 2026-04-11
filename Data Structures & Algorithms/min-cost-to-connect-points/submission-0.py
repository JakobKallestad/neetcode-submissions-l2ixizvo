class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        cost_map = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                y1, x1 = points[i]
                y2, x2 = points[j]
                dist = abs(y1-y2) + abs(x1-x2)
                cost_map[(i, j)] = dist
                cost_map[(j, i)] = dist
        
        sorted_costs = sorted(cost_map.items(), key=lambda x: x[1])

        n = len(points)
        parent = list(range(n))
        size = [1] * n  # union by size
        components = n  # optional: track how many sets remain
        res = 0

        def find(x: int) -> int:
            # Path compression
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path halving
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # already connected

            # Union by size (attach smaller to larger)
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            #components -= 1
            return True

        print(sorted_costs)
        for ij, c in sorted_costs:
            i, j = ij
            if union(i, j):
                res += c
        return res


# solution idea:
# get the cost between all points n^2
# sort it n*logn
# do a DRS
# only add the edges if they are not already connected.