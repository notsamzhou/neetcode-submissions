class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        if n == 1:
            return 1

        graph = {i: dict() for i in range(n)}
        for u, v, time in roads:
            graph[u][v] = time
            graph[v][u] = time


        cache = {}

        def dp(i):

            if i in cache:
                return cache[i]

            if i == n - 1:
                cache[i] = (0, 1)
                return cache[i]

            if i == n - 2:
                if n - 1 in graph[i]:
                    cache[i] = graph[i][n-1], 1

                else:
                    cache[i] = math.inf, 0

                return cache[i]



            min_dist = math.inf
            min_count = 0
            for j in range(i, n):

                if j in graph[i]:
                    dist, cnt = dp(j)
                    dist += graph[i][j]

                    if dist < min_dist:
                        min_dist = dist
                        min_count = cnt

                    elif dist == min_dist:
                        min_count += cnt

            
            cache[i] = (min_dist, min_count)
            return cache[i]

        dist, cnt = dp(0)

        return cnt % 1000000007
        
        