class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        visited = set()
        def dfs(crs):

            if preMap[crs] == [] or crs in visited:
                return True

            if crs in visiting:
                # Cycle detected
                return False

            
            

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.add(crs)
            return True

        for c in range(numCourses):

            if not dfs(c):
                return False
        return True