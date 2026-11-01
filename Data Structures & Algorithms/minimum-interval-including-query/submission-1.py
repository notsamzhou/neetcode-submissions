class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        for i in range(len(queries)):
            queries[i] = (i, queries[i])

        queries.sort(key = lambda x: (x[1], x[0]))
        intervals.sort(key = lambda x: (x[0], x[1]))

        curr_time = 0
        int_idx = 0
        min_heap = []
        res = [-1] * len(queries)

        for i in range(len(queries)):

            curr_time = queries[i][1]

            while int_idx < len(intervals) and intervals[int_idx][0] <= curr_time:
                interval = intervals[int_idx]
                heapq.heappush(min_heap, (interval[1] - interval[0] + 1, interval))
                int_idx += 1

            while min_heap and res[queries[i][0]] == -1:

                if min_heap[0][1][1] < queries[i][1]:
                    heapq.heappop(min_heap)
                    continue

                res[queries[i][0]] = min_heap[0][0]


        return res






        