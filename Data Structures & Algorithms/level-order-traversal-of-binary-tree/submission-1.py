# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        current_level = []
        next_level = None
        res = []

        while q:
            curr = q.popleft()
            current_level.append(curr.val)

            if curr.left:
                q.append(curr.left)
                if not next_level:
                    next_level = curr.left
            if curr.right:
                q.append(curr.right)

                if not next_level:
                    next_level = curr.right

            if not q or q[0] is next_level:
                res.append(current_level)
                current_level = []
                next_level = None

        return res
        