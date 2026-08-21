class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        neighbors = {}
        for i in range(len(equations)):
            
            if equations[i][0] not in neighbors:
                neighbors[equations[i][0]] = []

            if equations[i][1] not in neighbors:
                neighbors[equations[i][1]] = []

            neighbors[equations[i][0]].append((equations[i][1], values[i]))
            neighbors[equations[i][1]].append((equations[i][0], 1/values[i]))


        def dfs(curr_node, target, curr_val):

            if curr_node in visited:
                return -1

            if curr_node == target:
                return curr_val 


            visited.add(curr_node)

            if curr_node not in neighbors:
                return -1

            for neighbor, val in neighbors[curr_node]:
                ret = dfs(neighbor, target, curr_val * val)
                if ret != -1:
                    return ret

            return -1

        res = []

        for a, b in queries:
            if a not in neighbors or b not in neighbors:
                res.append(-1.0)
                continue
        
            visited = set()
            ret = dfs(a, b, 1)

            res.append(ret)

        return res