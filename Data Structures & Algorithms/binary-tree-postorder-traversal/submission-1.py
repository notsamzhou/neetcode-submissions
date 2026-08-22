# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        curr = root
        stack = []
        res = []

        while curr or stack:

            while curr:
                res.append(curr.val)

                if curr.left:
                    stack.append(curr.left)

                curr = curr.right

            if stack:
                curr = stack.pop()

        return res[::-1]
                
        