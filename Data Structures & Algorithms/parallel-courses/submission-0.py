class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        adj = {i: [] for i in range(1, n + 1)}
        indegree = {i: 0 for i in range(1, n + 1)}

        for prereq, nxt in relations:
            adj[prereq].append(nxt)
            indegree[nxt] += 1

        queue = deque()
        visited = set()

        for i in range(1, n   + 1):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)

        result = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        visited.add(nei)
                        queue.append(nei)


            result += 1

        if len(visited) != n:
            return -1

        return result


        