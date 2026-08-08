class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        res = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]

            else:
                prev_end = min(prev_end, interval[1])
                res += 1

        return res
        