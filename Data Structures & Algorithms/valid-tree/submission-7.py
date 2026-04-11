from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # need to dfs/bfs explore, but make sure to never to back the way we came from directly.
        # look for cycles.

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)

            for nbr in graph[i]:
                if nbr == prev:
                    continue
                if not dfs(nbr, i):
                    return False
            return True
        

        if not dfs(0, None):
            return False
        return len(visited) == n if n > 1 else not bool(edges)