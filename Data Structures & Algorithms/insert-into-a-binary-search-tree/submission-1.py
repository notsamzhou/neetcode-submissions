# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root
        prev = None

        while curr is not None:

            prev = curr
            if val > curr.val:
                curr = curr.right

            else:
                curr = curr.left

        newNode = TreeNode(val)
        if not prev:
            return newNode
        if val < prev.val:
            prev.left = newNode

        else:
            prev.right = newNode

        return root