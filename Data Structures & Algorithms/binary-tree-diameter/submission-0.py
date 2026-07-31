# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepthAndDiameter(root):

            if not root:
                return 0, 0

            ldepth, ldia = maxDepthAndDiameter(root.left)
            rdepth, rdia = maxDepthAndDiameter(root.right)

            return 1 + max(ldepth, rdepth), max(ldepth + rdepth, ldia, rdia)

        return maxDepthAndDiameter(root)[1]
        