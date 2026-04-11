"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        intervals = [(i.start, i.end) for i in intervals]
        if len(intervals) < 2:
            return True
        c, d = intervals[0]
        for a, b in intervals[1:]:
            if not (c < d <= a < b):
                return False
            c, d = a, b
        return True