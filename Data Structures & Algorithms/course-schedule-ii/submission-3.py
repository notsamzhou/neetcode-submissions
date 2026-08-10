class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)


        visiting = set()
        visited = set()
        res = []
        def dfs(curr):
            if curr in visited:
                return True

            if curr in visiting:
                return False

            visiting.add(curr)

            for nei in graph[curr]:
                if not dfs(nei):
                    return False

            visiting.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []
        if len(res) == numCourses:
            return res[::-1]

        return []