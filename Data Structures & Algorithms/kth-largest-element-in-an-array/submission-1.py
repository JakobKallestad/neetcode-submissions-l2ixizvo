import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        prev = float('inf')
        i = 0
        while i < k:
            current = heapq.heappop_max(heap)
            prev = current
            i += 1
        return current
            