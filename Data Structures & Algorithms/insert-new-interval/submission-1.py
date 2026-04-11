from collections import deque

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        queue = deque([(s, e) for s,e in intervals])
        res = []
        c, d = (newInterval[0], newInterval[1])
        while queue:
            a, b = queue.popleft()
            if not (a <= b < c <= d or c <= d < a <= b): # overlap
                c, d = min(a, c), max(b, d)
            else:
                res.append((a,b))
        
        for i, (a, b) in enumerate(res):
            if c < a:
                res.insert(i, (c,d))
                break
        if (c,d) not in res:
            return res + [(c,d)]
        return res






        