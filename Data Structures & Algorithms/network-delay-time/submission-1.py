class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        neighbors = dict()
        for u, v, t in times:
            if u not in neighbors:
                neighbors[u] = dict()

            neighbors[u][v] = t


        pq = []


        if k in neighbors:
            for v, t in neighbors[k].items():
                heapq.heappush(pq, (t, v))

        dist = [float('inf') for i in range(n + 1)]
        dist[k] = 0
        while pq:

            time, u = heapq.heappop(pq)
            if dist[u] < float('inf'):
                continue
            
            dist[u] = time

            if u in neighbors:
                for v, t in neighbors[u].items():
                    heapq.heappush(pq, (t + time, v))

        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1

        