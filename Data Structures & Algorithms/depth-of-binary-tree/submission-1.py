# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node, curr_depth):
            if not node:
                return curr_depth


            return max(depth(node.left, curr_depth + 1), depth(node.right, curr_depth + 1))

        return depth(root, 0)