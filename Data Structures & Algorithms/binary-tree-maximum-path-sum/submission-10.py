# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root:
                return -float('inf'), -float('inf')

            leftMax, leftMaxInc = dfs(root.left)
            rightMax, rightMaxInc = dfs(root.right)

            total = root.val + max(leftMaxInc, 0) + max(rightMaxInc, 0)
            inc = root.val + max(max(leftMaxInc, 0), max(rightMaxInc, 0))
            res = max(res, total)
            return total, inc

        dfs(root)
        return res