from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a

        state = [0] * numCourses  # 0 unvisited, 1 visiting, 2 done

        def dfs(u: int) -> bool:
            if state[u] == 1:     # back-edge found
                return False
            if state[u] == 2:     # already checked
                return True

            state[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
