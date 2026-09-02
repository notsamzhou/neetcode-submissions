# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {}
        def dp(curr, canRob):
            if curr is None:
                return 0

            if (curr, canRob) in cache:
                return cache[(curr, canRob)]

            skip = dp(curr.left, True) + dp(curr.right, True)
            if not canRob:
                cache[(curr, canRob)] = skip
                return skip

            cache[(curr, canRob)] =  max(curr.val + dp(curr.left, False) + dp(curr.right, False), skip)
            return cache[(curr, canRob)]

        return dp(root, True)
        