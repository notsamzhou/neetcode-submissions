# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        # each child has to return the longest sequence ending at itself and the longest in its subtree

        def dp_helper(curr):
            if curr is None:
                return 0, 0


            lMax, lInc = dp_helper(curr.left)
            rMax, rInc = dp_helper(curr.right)

            currInc = 1

            if curr.left and curr.left.val == curr.val + 1:
                currInc = 1 + lInc

            if curr.right and curr.right.val == curr.val + 1:
                currInc = max(currInc, 1 + rInc)

            currMax = max(currInc, lMax, rMax)

            return currMax, currInc

        res, _ = dp_helper(root)

        return res
        