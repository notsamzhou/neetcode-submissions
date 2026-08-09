class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return False

            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor != parent:
                    if not dfs(neighbor, curr):
                        return False


            return True

        no_cycle = dfs(0, None)

        return no_cycle and visited == set([i for i in range(n)])

        