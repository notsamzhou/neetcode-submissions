class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

        self.num_comp = n
        

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x
        

    def isSameComponent(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        return p1 == p2


    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
            
        self.num_comp -= 1
        return True

        

    def getNumComponents(self) -> int:
        return self.num_comp

