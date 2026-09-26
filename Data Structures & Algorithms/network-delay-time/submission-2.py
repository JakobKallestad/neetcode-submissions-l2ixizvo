class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (u, v, t) in times:
            graph[u].append((v, t))
        
        pq = [(0, k)]

        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        while pq:
            c_time, c_node = heapq.heappop(pq)  # minimum time pop
            if c_time > dist[c_node]:
                continue

            for (n_node, e_time) in graph[c_node]:
                n_time = e_time+c_time
                if n_time < dist[n_node]:
                    dist[n_node] = n_time
                    heapq.heappush(pq, (n_time, n_node))
        
        min_time = max(dist.values())
        return -1 if min_time == float('inf') else min_time