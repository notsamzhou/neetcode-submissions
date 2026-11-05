class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        #UF that tracks the number of each value in the component

        n = len(vals)

        parent = [i for i in range(n)]
        counts = [{vals[i]: 1} for i in range(n)]
        size = [1 for i in range(n)]

        res = n

        def find(x):

            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return parent[x]

        def union(u, v):
            nonlocal res
            x, y = find(u), find(v)

            if x == y:
                return

            bottleneck = max(vals[u], vals[v])
            res += counts[x].get(bottleneck, 0) * counts[y].get(bottleneck, 0)


            if size[x] >= size[y]:
                for val in counts[y]:
                    counts[x][val] = counts[x].get(val, 0) + counts[y][val]

                size[x] += size[y]
                parent[y] = x

            else:
                for val in counts[x]:
                    counts[y][val] = counts[y].get(val, 0) + counts[x][val]

                size[y] += size[x]
                parent[x] = y


        edges.sort(key = lambda x: max(vals[x[0]], vals[x[1]]))

        for u, v in edges:
            union(u, v)

        return res
            
