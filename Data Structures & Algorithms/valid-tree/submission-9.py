from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(i: int, prev: int) -> bool:
            if i in visited:
                return False
            visited.add(i)
            for nbr in graph[i]:
                if nbr == prev:
                    continue
                if not dfs(nbr, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
