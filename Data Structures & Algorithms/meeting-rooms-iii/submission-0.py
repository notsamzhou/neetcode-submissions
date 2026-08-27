class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        start_pq = [i for i in range(n)]
        finishing_pq = []

        res = [0 for i in range(n)]

        for meeting in meetings:

            while finishing_pq and finishing_pq[0][0] <= meeting[0]:
                _, idx = heapq.heappop(finishing_pq)
                heapq.heappush(start_pq, (idx))

            if not start_pq:
                new_start = finishing_pq[0][0]
                new_end = meeting[1] + finishing_pq[0][0] - meeting[0]
                _, idx = heapq.heappop(finishing_pq)
                heapq.heappush(finishing_pq, (new_end, idx))
                res[idx] += 1

            else:
                idx = heapq.heappop(start_pq)
                heapq.heappush(finishing_pq, (meeting[1], idx))

                res[idx] += 1

        maximum = 0
        max_idx = 0
        for i in range(n):
            if res[i] > maximum:
                max_idx = i
                maximum = res[i]

        return max_idx



                





        
        