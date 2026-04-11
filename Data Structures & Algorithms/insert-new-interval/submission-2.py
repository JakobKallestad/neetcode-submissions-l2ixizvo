from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        c, d = newInterval
        res: List[Tuple[int, int]] = []

        for a, b in intervals:
            # If [a,b] and [c,d] overlap, merge into [c,d]
            if a <= d and c <= b:
                c = min(c, a)
                d = max(d, b)
            else:
                res.append((a, b))

        # res is still sorted by start because we kept original order
        # Insert merged interval in the right place by start
        idx = bisect_left(res, (c, d))  # tuple ordering: compares by start, then end
        res.insert(idx, (c, d))

        # Return as List[List[int]] if you want to match the signature strictly
        return [list(x) for x in res]
