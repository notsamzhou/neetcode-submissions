# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx = dict()
        for i in range(len(inorder)):
            inorder_idx[inorder[i]] = i

        curr = len(inorder) - 1
        def build_tree(l, r):
            
            nonlocal curr
            if l > r:
                return None

            root = TreeNode(postorder[curr])

            curr -= 1

            root.right = build_tree(inorder_idx[root.val] + 1, r)
            root.left = build_tree(l, inorder_idx[root.val] - 1)

            return root



        return build_tree(0, len(inorder) - 1)