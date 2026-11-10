# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(curr, lower, upper):
            if not curr:
                return True

            if not lower < curr.val < upper:
                return False

            return validate(curr.left, lower, curr.val) and validate(curr.right, curr.val, upper)

        return validate(root, -math.inf, math.inf)
        