"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)
        intervals = [(i.start, i.end) for i in intervals]

        n_days = 0
        remaining_intervals = [None, None]
        while len(remaining_intervals) > 1:
            n_days += 1
            remaining_intervals = []
            c, d = intervals[0]
            for a, b in intervals[1:]:
                if a >= d:
                    c, d = a, b
                else:
                    remaining_intervals.append((a, b))
            intervals = remaining_intervals
        if remaining_intervals:
            n_days += 1

        return n_days