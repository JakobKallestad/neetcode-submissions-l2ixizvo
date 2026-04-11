import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            y, x = p
            distances.append(((y**2 + x**2)**0.5, p))
        #heap = distances
        #heapq.heapify(heap)
        distances = sorted(distances, key=lambda x: x[0])
        return [d[1] for d in distances[:k]]

