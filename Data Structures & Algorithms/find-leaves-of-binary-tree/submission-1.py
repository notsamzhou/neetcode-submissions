# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        def getHeight(node):
            if node is None:
                return -1


            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            height = max(left_height, right_height) + 1

            if len(result) == height:
                result.append([])

            result[height].append(node.val)
            return height

        getHeight(root)

        return result
        


        