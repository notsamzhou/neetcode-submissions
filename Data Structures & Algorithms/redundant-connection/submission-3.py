class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        queue = deque()

        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        for i in range(1, n + 1):
            if indegree[i] == 1:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            indegree[curr] -= 1

            for v in adj[curr]:
                indegree[v] -= 1

                if indegree[v] == 1:
                    queue.append(v)


        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]

        return []