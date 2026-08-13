class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = {}
        for u, v, cost in edges:
            if u not in adj:
                adj[u] = []

            adj[u].append((cost, v))

        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        heap = [(0, src)]
        visited = set()

        while heap:
            final, u = heapq.heappop(heap)

            if u not in visited:
                visited.add(u)
                dist[u] = final

                if u in adj:

                    for cost, v in adj[u]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            heapq.heappush(heap, (dist[u] + cost, v))

        res = {}
        for i in range(n):
            res[i] = dist[i] if dist[i] != float('inf') else -1

        return res



