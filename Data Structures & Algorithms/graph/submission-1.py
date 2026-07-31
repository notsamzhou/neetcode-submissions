class Graph:
    
    def __init__(self):
        self.hashmap = dict()


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.hashmap:
            self.hashmap[src] = set()
        if dst not in self.hashmap:
            self.hashmap[dst] = set()

        self.hashmap[src].add(dst) 


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.hashmap and dst in self.hashmap[src]:
            self.hashmap[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)

    
    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.hashmap[src]:
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
            
        return False

