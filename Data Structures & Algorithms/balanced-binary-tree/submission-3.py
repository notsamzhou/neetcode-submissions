# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node):
            if node is None:
                return 0

            l_height = height(node.left)
            if l_height == -1:
                return -1
            r_height = height(node.right)
            if r_height == -1:
                return -1

            if abs(l_height - r_height) > 1:
                return -1

            return 1 + max(l_height, r_height)


        return height(root) != -1
        