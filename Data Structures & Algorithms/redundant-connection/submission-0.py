class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        
        graph = defaultdict(list)

        for edge in reversed(edges):
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False] * (len(edges) + 1)


        cycle = set()
        cycle_start = -1
        
        def dfs(node, parent):
            nonlocal cycle_start

            visited[node] = True

            for neighbor in graph[node]:
                if visited[neighbor] and neighbor != parent:
                    cycle.add(node)
                    cycle_start = neighbor
                    return True

                if neighbor == parent:
                    continue
                
                if dfs(neighbor, node):
                    if cycle_start != -1:
                        cycle.add(node)

                    if node == cycle_start:
                        cycle_start = -1
                    return True

            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
                    



        