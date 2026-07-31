class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(u, v):
            x, y = find(u), find(v)
            if x == y:
                return False


            if rank[x] > rank[y]:
                parent[y] = x

            elif rank[y] > rank[x]:
                parent[x] = y

            else:
                parent[y] = x
                rank[x] += 1

            return True

        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1

        return components
