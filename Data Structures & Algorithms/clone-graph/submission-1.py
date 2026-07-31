"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        visited = set()
        def dfs(node):
            visited.add(node)

            if node not in oldToNew:
                copy = Node(node.val)
                oldToNew[node] = copy

            copy = oldToNew[node]

            for nei in node.neighbors:
                if nei not in visited:
                    copy.neighbors.append(dfs(nei))
                else:
                    copy.neighbors.append(oldToNew[nei])
            return copy

        return dfs(node) if node else None