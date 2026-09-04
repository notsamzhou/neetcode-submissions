# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        

        def validateAndReturnLargest(root):

            if root is None:
                return math.inf, -math.inf, 0

            lMin, lMax, lSize = validateAndReturnLargest(root.left)
            rMin, rMax, rSize = validateAndReturnLargest(root.right)

            if lMax < root.val < rMin:
                largest = 1 + lSize + rSize
                currMin = min(lMin, root.val)
                currMax = max(rMax, root.val)
                return currMin, currMax, largest
            else:
                largest = max(lSize, rSize)

                return -math.inf, math.inf, largest

            

        return validateAndReturnLargest(root)[2]
