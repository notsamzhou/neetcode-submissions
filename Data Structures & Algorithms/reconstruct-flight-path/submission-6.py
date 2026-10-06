class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append((v, False))


        airports = graph.keys()
        for airport in airports:
            graph[airport] = sorted(graph[airport])
        res = []
        def dfs(curr):


            for i, (dest, used) in enumerate(graph[curr]):
                if not used:
                    graph[curr][i] = (dest, True)
                    dfs(dest)

            res.append(curr)



        dfs("JFK")
        return res[::-1]
        