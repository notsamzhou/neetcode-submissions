class Solution:

    def dfs(self, curr, graph, visited, topo_sort, path):

        visited.add(curr)
        path.add(curr)
        

        for neighbor in graph[curr]:
            if neighbor in path:
                return False
            
            if neighbor not in visited:
                
                
                if not self.dfs(neighbor, graph, visited, topo_sort, path):
                    return False

        path.remove(curr)
        topo_sort.append(curr)
        return True

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        rev = {i: [] for i in range(n)}
        for u, v in edges:
            rev[v].append(u)


        visited = set()
        topo_sort = []

        for i in range(n):
            path = set()
            if i not in visited:
                if not self.dfs(i, rev, visited, topo_sort, path):
                    return []
             


        return topo_sort
        