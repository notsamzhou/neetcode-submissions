class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(colors)
        distance = [[n] * 4 for _ in colors]
        for color in range(1, 4):
            last = -n
            for i in range(n):
                if colors[i] == color: last = i
                distance[i][color] = min(distance[i][color], i - last)

            last = 2 * n
            for i in range(n - 1, -1, -1):
                if colors[i] == color: last = i
                distance[i][color] = min(distance[i][color], last - i)

        
        return [distance[i][c] if distance[i][c] != n else -1 for (i, c) in queries]
