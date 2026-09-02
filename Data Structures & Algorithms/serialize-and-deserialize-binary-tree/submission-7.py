# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = ""
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr:
                res += f"#{curr.val}"

                queue.append(curr.left)
                queue.append(curr.right)

            else:
                res += "#\\"

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


        vals = data.split("#")[1:]

        if vals[0] == "\\":
            return None

        root = TreeNode(vals[0])
        i = 1
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if i < len(vals) and vals[i] != "\\":
                curr.left = TreeNode(vals[i])
                queue.append(curr.left)

            i += 1

            if i < len(vals) and vals[i] != "\\":
                curr.right = TreeNode(vals[i])
                queue.append(curr.right)

            i += 1

        return root


