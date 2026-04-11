class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        n_remove = 0
        c, d = intervals[0]

        for a, b in intervals[1:]:
            if a >= d:
                c, d = a, b
            else:
                n_remove += 1

        return n_remove
