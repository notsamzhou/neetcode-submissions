class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        finished = set()
        visiting = set()
        def dfs(i, parent):

            if i in finished:
                return None

            if i in visiting:
                return i

            visiting.add(i)

            for nei in graph[i]:
                if nei != parent:
                    cycle_start = dfs(nei, i)

                    if cycle_start == i:
                        cycle_start = None
                        return cycle_start

                    if cycle_start is not None:
                        return cycle_start


            visiting.remove(i)
            finished.add(i)

        dfs(1, -1)

        
        for edge in reversed(edges):
            if edge[0] in visiting and edge[1] in visiting:
                return edge

