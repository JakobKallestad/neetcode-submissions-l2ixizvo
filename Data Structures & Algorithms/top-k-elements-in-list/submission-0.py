class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_counter = defaultdict(int)
        heap = [(0, None)]*k
        for n in nums:
            n_counter[n] += 1
        
        for k, v in n_counter.items():
            heapq.heappushpop(heap, (v, k))
        print(heap)
        return [e[1] for e in heap]
