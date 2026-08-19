# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dp(curr, can_rob):
            if not curr:
                return 0

            if (curr, can_rob) in cache:
                return cache[(curr, can_rob)]



            cache[(curr, can_rob)] = dp(curr.left, True) + dp(curr.right, True)
            if can_rob:
                cache[(curr, can_rob)] = max(cache[(curr, can_rob)], dp(curr.left, False) + dp(curr.right, False) + curr.val)

            return cache[(curr, can_rob)]

        return max(dp(root, True), dp(root,False))
        