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
                return True, math.inf, -math.inf, 0

            lValid, lMin, lMax, lSize = validateAndReturnLargest(root.left)
            rValid, rMin, rMax, rSize = validateAndReturnLargest(root.right)

            if lValid and rValid and lMax < root.val < rMin:
                largest = 1 + lSize + rSize
                currMin = min(lMin, root.val)
                currMax = max(rMax, root.val)
                return True, currMin, currMax, largest
            else:
                largest = max(lSize, rSize)

                return False, -math.inf, math.inf, largest

            

        return validateAndReturnLargest(root)[3]
