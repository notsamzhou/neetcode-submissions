# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:


        def dfs(root):
            if not root:
                return False, []

            if not root.left and not root.right:
                return True, [root.val]

            prune, leaves_r = dfs(root.left)
            if prune:
                root.left = None

            prune, leaves_l = dfs(root.right)
            if prune:
                root.right = None


            return False, leaves_l + leaves_r

        result = []
        while root.left or root.right:
            _, leaves = dfs(root)
            result.append(leaves)

        result.append([root.val])
        return result


        


        