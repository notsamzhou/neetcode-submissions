class TreeNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return

        prev = None
        curr = self.root
        while curr is not None:
            prev = curr
            if curr.key > key:
                
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                curr.val = val
                return


        if prev.key > key:
            prev.left = new_node

        else:
            prev.right = new_node


    def get(self, key: int) -> int:
        prev = None
        curr = self.root
        while curr is not None:
            prev = curr
            if curr.key > key:
                
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val

        return -1


    def getMin(self) -> int:
        m = self._getMin(self.root)
        return m.val if m else -1
        

    def _getMin(self, curr):
        if not curr:
            return None

        prev = None
        while curr:
            prev = curr
            curr = curr.left

        return prev


    def getMax(self) -> int:
        if not self.root:
            return -1
            
        prev = None
        curr = self.root
        while curr:
            prev = curr
            curr = curr.right

        return prev.val


    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)

    def remove_helper(self, curr, key):
        if not curr:
            return None

        if curr.key > key:
            curr.left = self.remove_helper(curr.left, key)
        elif curr.key < key:
            curr.right = self.remove_helper(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left

            else:
                successor = self._getMin(curr.right)
                curr.key = successor.key
                curr.val = successor.val

                curr.right = self.remove_helper(curr.right, successor.key)

        return curr



    def getInorderKeys(self) -> List[int]:
        curr = self.root
        stack = []
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.key)

            curr = curr.right

        return res


