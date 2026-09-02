class UnionFind:

    def __init__(self, z):
        self.parent = [i for i in range(z)]
        self.rank = [1] * (z + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        u, v = self.find(x), self.find(y)

        if u == v:
            return False

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u

        elif self.rank[u] < self.rank[v]:
            self.parent[u] = v

        else:
            self.parent[v] = u
            self.rank[u] += 1

        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        uf = UnionFind(m * n)

        res = 0

        out = []
        islands = set()
        for r, c in positions:

            idx = r * n + c

            if idx in islands:
                out.append(out[-1])
                continue


            res += 1
            islands.add(idx)


            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n:
                    n_idx = nr * n + nc



                    if n_idx in islands and uf.union(idx, n_idx):


                        res -= 1

            out.append(res)
        return out

