from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a

        visiting = set()   # nodes in current DFS stack
        visited = set()    # nodes fully processed
        order = []         # postorder; reverse at end

        def dfs(u: int) -> bool:
            if u in visiting:     # cycle
                return False
            if u in visited:      # already done
                return True

            visiting.add(u)
            for v in graph[u]:
                if not dfs(v):
                    return False
            visiting.remove(u)

            visited.add(u)
            order.append(u)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order[::-1]
