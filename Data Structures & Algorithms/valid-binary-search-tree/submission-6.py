# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def bstHelper(curr):

            if not curr:
                return True, None, None

            lValid, lMin, lMax = bstHelper(curr.left)

            rValid, rMin, rMax = bstHelper(curr.right)

            if not lValid or not rValid:
                return False, None, None


            if lMax is not None and lMax >= curr.val:
                return False, None, None

            if rMin is not None and rMin <= curr.val:
                return False, None, None

            currMin, currMax = curr.val, curr.val
            if lMin is not None:
                currMin = lMin

            if rMax is not None:
                currMax = rMax

            return True, currMin, currMax

        res = bstHelper(root)
        return res[0]


        