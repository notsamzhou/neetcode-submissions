class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        class UnionFind:
            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.rank = [1] * n

            def find(self, v1):
                while v1 != self.par[v1]:
                    self.par[v1] = self.par[self.par[v1]]
                    v1 = self.par[v1]
                return v1

            def union(self, v1, v2):
                p1, p2 = self.find(v1), self.find(v2)
                if p1 == p2:
                    return False
                if self.rank[p1] > self.rank[p2]:
                    self.par[p2] = p1
                    self.rank[p1] += self.rank[p2]
                else:
                    self.par[p1] = p2
                    self.rank[p2] += self.rank[p1]
                return True


        mst = [[] for _ in range(n)]
        mst_edges = []

        edge_list = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edge_list.sort()


        uf = UnionFind(n)
        for w, u, v, i in edge_list:
            if uf.union(u, v):
                mst[u].append((v, i))
                mst[v].append((u, i))
                mst_edges.append(i)


        def dfs(node):

            for neighbor, i in mst[node]:
                if path and i == path[-1]:
                    continue

                path.append(i)
                if neighbor == dest or dfs(neighbor):
                    return True

                path.pop()

            return False


        pseudo, mst_edges = set(), set(mst_edges)
        for i in range(len(edges)):
            if i in mst_edges:
                continue

            path, dest = [], edges[i][1]
            dfs(edges[i][0])

            for j in path:
                if edges[i][2] == edges[j][2]:
                    pseudo.add(i)
                    pseudo.add(j)
        

        return [list(mst_edges - pseudo), list(pseudo)]


