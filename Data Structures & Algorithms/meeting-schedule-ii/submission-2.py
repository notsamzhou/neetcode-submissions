"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res