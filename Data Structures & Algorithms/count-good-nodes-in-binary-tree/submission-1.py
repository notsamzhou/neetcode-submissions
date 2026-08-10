# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, biggest):
            if not curr:
                return 0

            res = dfs(curr.left, max(biggest, curr.val))
            res += dfs(curr.right, max(biggest, curr.val))

            if biggest <= curr.val:
                res += 1

            return res

        return dfs(root, float("-inf"))