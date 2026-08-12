class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        visited = set()
        heap = [(0, 0)]
        res = 0
        while heap and len(visited) != len(points):
            cost, x = heapq.heappop(heap)
            if x not in visited:
                res += cost
                visited.add(x)

                for i in range(len(points)):
                    if i != x:
                        p1 = points[x]
                        p2 = points[i]
                        dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                        heapq.heappush(heap, (dist, i))

        return res
        