class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []

        curr = 0
        while curr < len(intervals) and intervals[curr][1] < newInterval[0]:
            res.append(intervals[curr])
            curr += 1

        
        while curr < len(intervals) and (newInterval[1] >= intervals[curr][0]):
            newInterval[0] = min(intervals[curr][0], newInterval[0])
            newInterval[1] = max(intervals[curr][1], newInterval[1])

            curr += 1

        res.append(newInterval)

        while curr < len(intervals):
            res.append(intervals[curr])
            curr += 1
        
        return res