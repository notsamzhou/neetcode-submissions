class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        class UnionFind:

            def __init__(self, n):
                self.parent = [i for i in range(n + 1)]
                self.rank = [1] * (n + 1)
                self.n_components = n

            def find(self, x): 

                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]

                return x

            def union(self, u, v):
                p1, p2 = self.find(u), self.find(v)

                if p1 == p2:
                    return False

                if self.rank[p1] > self.rank[p2]:
                    self.parent[p2] = p1

                elif self.rank[p2] > self.rank[p1]:
                    self.parent[p1] = p2

                else:
                    self.parent[p2] = p1
                    self.rank[p1] += 1

                self.n_components -= 1

                return True

        for i, (u, v, w) in enumerate(edges):
            edges[i] = [i, u, v, w]

        edges.sort(key = lambda x: x[3])
        # Find an MST using Kruskal's to get MST weight

        uf = UnionFind(n)
        mst_weight = 0
        for i, u, v, w in edges:
            if uf.union(u, v):
                mst_weight += w



        # Iterate through all edges and find if the edge is critical or pseudo
        critical, pseudo = [], []
        for i, u, v, w, in edges:
            uf = UnionFind(n)

            test_weight = 0
            for j, x, y, z in edges:
                if i == j:
                    continue
                if uf.union(x, y):
                    test_weight += z

            if uf.n_components > 1 or test_weight > mst_weight:
                critical.append(i)

            else:
                uf = UnionFind(n)
                uf.union(u, v)

                test_weight = w
                for j, x, y, z in edges:
                    if uf.union(x, y):
                        test_weight += z

                if uf.n_components == 1 and test_weight == mst_weight:
                    pseudo.append(i)

        return [critical, pseudo]
            


            
