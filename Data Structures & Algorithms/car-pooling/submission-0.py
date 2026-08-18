class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key = lambda x: x[1])

        passengers = 0
        pq = []
        for trip in trips:

            while pq and trip[1] >= pq[0][1][2]:
                end, past_trip = heapq.heappop(pq)
                passengers -= past_trip[0]

            if trip[0] + passengers > capacity:
                return False

            heapq.heappush(pq, (trip[2], trip))   
            passengers += trip[0]

        return True         
        