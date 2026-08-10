# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"

        res = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if not curr:
                res.append("#")

            else:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)

        return '\\'.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split('\\')
        if nodes[0] == "#":
            return None

        queue = deque()
        root = TreeNode(int(nodes[0]))
        queue.append(root)

        i = 1
        while queue:
            curr = queue.popleft()

            if nodes[i] != "#":
                curr.left = TreeNode(int(nodes[i]))
                queue.append(curr.left)
            i += 1
            if nodes[i] != "#":
                curr.right = TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i += 1
        return root


            
