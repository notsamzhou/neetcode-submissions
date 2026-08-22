class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        neighbors = {i: [] for i in range(n)}
        for u, v in edges:


            neighbors[u].append(v)
            neighbors[v].append(u)

        dp = [[0] * 2 for _ in range(n)]
        # dp[i] = length of the longest two paths to a leaf in a tree rooted at 0

        def downward(i):


            visited.add(i)

            for j in neighbors[i]:

                if j not in visited:
                    downward(j)

                    height = 1 + dp[j][0]

                    if height > dp[i][0]:
                        dp[i][1] = dp[i][0]
                        dp[i][0] = height

                    elif height > dp[i][1]:
                        dp[i][1] = height

        def upward(i, upwardDist):


            visited.add(i)

            if upwardDist > dp[i][0]:
                dp[i][1] = dp[i][0]
                dp[i][0] = upwardDist

            elif upwardDist > dp[i][1]:
                dp[i][1] = upwardDist

            for j in neighbors[i]:
                if j not in visited:
                    toChild = 1 + (dp[i][1] if dp[j][0] + 1 == dp[i][0] else dp[i][0])
                    upward(j, toChild)

        visited = set()
        downward(0)
        visited = set()
        upward(0, 0)

        minHgt, res = n, []
        for i in range(n):
            minHgt = min(minHgt, dp[i][0])


        for i in range(n):
            if minHgt == dp[i][0]:
                res.append(i)

        return res



        