import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        prev = float('inf')
        i = 0
        while heap:
            current = heapq.heappop_max(heap)
            if i == k:
                return prev
            prev = current
            i += 1
        return current
            