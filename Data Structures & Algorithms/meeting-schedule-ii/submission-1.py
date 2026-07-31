"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x: x.start)
        minheap = []

        res = 0

        for i in range(len(intervals)):
            while minheap and minheap[0] <= intervals[i].start:
                heapq.heappop(minheap)

                
            heapq.heappush(minheap, intervals[i].end)

            res = max(res, len(minheap))

        return res

        