class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        graph = {i: list() for i in range(n)}
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        #dp[i][j] = minimum edit distance of a path ending at city j, matching from i: in targetPath
        
        dp = [[n] * n for _ in range(len(targetPath))]
        for i in range(n):
            if names[i] == targetPath[-1]:
                dp[-1][i] = 0
            else:
                dp[-1][i] = 1

        for i in range(len(targetPath) - 2, -1, -1):
            target = targetPath[i]

            for c in range(n):
                dp[i][c] = int(names[c] != target) + min(dp[i+1][v] for v in graph[c])

            
        print(targetPath)
        print(dp)
            

        #find path
        curr = min(range(n), key=lambda v: dp[0][v])
        ans = [curr]

        for i in range(1, len(targetPath)):
            curr = min(graph[curr], key=lambda v: dp[i][v])

            ans.append(curr)

        return ans
            

            
            




