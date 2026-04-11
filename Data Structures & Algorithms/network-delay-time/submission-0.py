from collections import defaultdict, deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()

        graph = defaultdict(list)
        for t in times:
            ui, vi, ti = t
            graph[ui].append((vi, ti))
        
        queue = deque()
        queue.append(k)

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            for nbr in graph[current]:
                vi, ti = nbr
                queue.append(vi)
        
        if len(visited) != n:
            return -1

        dist = {k: 0}
        pq = [(0, k)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist.get(u, float("inf")):
                continue  # stale entry

            for v, w in graph.get(u, []):
                nd = d + w
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        return max(dist.values())
                



# Thinking:
# Can check feasability first. Going from 1 to try to reach all the nodes with DFS/BFS should be pretty fast.
