class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1


        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)


        res = []
        while queue:
            course = queue.popleft()

            res.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) == numCourses:
            return res

        return []
        