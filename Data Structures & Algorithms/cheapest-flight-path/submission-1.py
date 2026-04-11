import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # You can take at most k stops => at most k+1 edges
        max_edges = k + 1

        # dist[node][edges_used] = cheapest cost to reach node using exactly edges_used edges
        INF = float("inf")
        dist = [[INF] * (max_edges + 1) for _ in range(n)]
        dist[src][0] = 0

        # (cost_so_far, node, edges_used)
        pq = [(0, src, 0)]

        while pq:
            cost, node, edges = heapq.heappop(pq)

            # Skip if this is a stale heap entry
            if cost != dist[node][edges]:
                continue

            # Because this is Dijkstra, the first time we pop dst is optimal under constraints
            if node == dst:
                return cost

            if edges == max_edges:
                continue  # can't take more flights

            for nxt, w in graph[node]:
                new_cost = cost + w
                new_edges = edges + 1
                if new_cost < dist[nxt][new_edges]:
                    dist[nxt][new_edges] = new_cost
                    heapq.heappush(pq, (new_cost, nxt, new_edges))

        return -1
