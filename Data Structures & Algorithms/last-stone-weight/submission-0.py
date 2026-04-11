import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)
        
        while len(max_heap) > 1:
            x = heapq.heappop_max(max_heap)
            y = heapq.heappop_max(max_heap)
            if x < y:
                heapq.heappush_max(max_heap, y-x)
            elif x > y:
                heapq.heappush_max(max_heap, x-y)

        if max_heap:
            return max_heap[0]
        else:
            return 0
