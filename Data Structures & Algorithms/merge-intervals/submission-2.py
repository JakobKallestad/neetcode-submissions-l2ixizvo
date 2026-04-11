class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        c, d = intervals[0]
        i = 1
        merged = True
        while i < len(intervals):
            a, b = intervals[i]
            if not (d < a):  # overlap
                c, d = min(a, c), max(b, d)
                merged = True
            else:
                res.append((c, d))
                if i+1 < len(intervals):
                    c,d = intervals[i]
                merged = False
            i += 1
    
        return res+[(c,d)] if merged else res+[(a,b)]

