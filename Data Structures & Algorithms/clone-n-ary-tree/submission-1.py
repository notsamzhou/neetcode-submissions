"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        copyDict = {}


        def dfs(curr):
            if curr in copyDict:
                return copyDict[curr]

            if curr is None:
                return None

            node = Node(curr.val)
            copyDict[curr] = node
            for child in curr.children:
                node.children.append(dfs(child))

            return node

        
        return dfs(root)

        