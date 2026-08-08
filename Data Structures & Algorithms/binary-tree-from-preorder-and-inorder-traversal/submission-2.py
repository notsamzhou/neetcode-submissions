# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_idx = dict()
        for i in range(len(inorder)):
            inorder_idx[inorder[i]] = i


        curr = 0
        def build_dfs(start, end):
            nonlocal curr

            if start > end:
                return None

            root = TreeNode(val = preorder[curr])

            curr += 1
            root.left = build_dfs(start, inorder_idx[root.val] - 1)
            root.right = build_dfs(inorder_idx[root.val] + 1, end)
            return root

        return build_dfs(0, len(inorder) - 1)