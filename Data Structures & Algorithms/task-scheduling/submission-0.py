import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks2 = defaultdict(int)
        for t in tasks:
            tasks2[t] += 1
        heap = list(tasks2.values())
        heapq.heapify_max(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                current = heapq.heappop_max(heap)
                if current-1 > 0:
                    queue.append((current-1, time+n))

            if queue and time == queue[0][1]:
                c, _ = queue.popleft()
                heapq.heappush_max(heap, c)
        return time
         




