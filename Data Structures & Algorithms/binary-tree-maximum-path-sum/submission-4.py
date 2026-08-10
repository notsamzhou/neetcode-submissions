# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # state at node i is the maximum ending from the left, ending from the right, and in the entire subtree

        def helper(curr):

            if not curr:
                return 0, 0, 0

            if not curr.left and not curr.right:

                return curr.val, curr.val, curr.val

            if curr.left:
                lcLeft, lcRight, lc = helper(curr.left)
            else:
                lcLeft, lcRight, lc = -float('inf'), -float('inf'), -float('inf')

            if curr.right:
                rcLeft, rcRight, rc = helper(curr.right)
            else:
                rcLeft, rcRight, rc = -float('inf'), -float('inf'), -float('inf')

            left = max(curr.val, curr.val + max(lcLeft, lcRight))
            right = max(curr.val, curr.val + max(rcLeft, rcRight))

            total = max([left, right, lc, rc, left + rcLeft, left + rcRight, right + lcLeft, right + lcRight, curr.val])

            return left, right, total

        _, _, res = helper(root)


        return res



        