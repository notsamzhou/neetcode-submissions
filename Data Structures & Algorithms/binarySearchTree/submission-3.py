class TreeNode:
    def __init__(self, key = None, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)

        else:
            prev = self.root
            curr = self.root

            while curr:
                prev = curr
                if key > curr.key:
                    curr = curr.right

                elif key < curr.key:
                    curr = curr.left
                else:
                    curr.val = val
                    return

            new_node = TreeNode(key, val)
            if key > prev.key:
                prev.right = new_node

            else:
                prev.left = new_node

        
        
        


    def get(self, key: int) -> int:

        curr = self.root
        while curr:
            if curr.key == key:
                return curr.val

            elif curr.key < key:
                curr = curr.left
            else:
                curr = curr.right

        return -1


    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left

        return curr.val if curr else -1


    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right

        return curr.val if curr else -1


    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right

        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left

        return root

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
        

    def removeHelper(self, root, key):
        if not self.root:
            return None

        if key > root.key:
            root.right = self.removeHelper(root.right, key)

        elif key < root.key:
            root.left = self.removeHelper(root.left, key)

        else:
            if not root.left and not root.right:
                root = None

            elif root.right:
                succ = self.successor(root)
                root.val = succ.val
                root.key = succ.key
                root.right = self.removeHelper(root.right, root.key)

            else:
                pred = self.predecessor(root)
                root.val = pred.val
                root.key = pred.key
                root.left = self.removeHelper(root.left, root.key)

        return root


    def getInorderKeys(self) -> List[int]:
        result = []
        stack = []

        curr = self.root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop(-1)
            result.append(curr.key)
            curr = curr.right
        
        return result

    

