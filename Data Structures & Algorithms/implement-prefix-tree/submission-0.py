class TrieNode:
    def __init__(self):
        self.children = dict()

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.children['finished'] = True

    def search(self, word: str) -> bool:

        curr = self.root
        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        
        return 'finished' in curr.children
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return True
        