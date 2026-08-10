class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        dist[src] = 0

        for i in range(k+1):
            temp = dist.copy()
            for (u, v, d) in flights:
                if dist[u] + d < dist[v]:
                    temp[v] = min(temp[v], dist[u] + d)


            dist = temp
        
        return dist[dst] if dist[dst] != float('inf') else -1
