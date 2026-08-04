# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p
            p, q = q, temp

        
        if root.val == p.val or root.val == q.val:
            return root

        if root.val > p.val and root.val < q.val:
            return root
        
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)
        

            


        