class TrieNode:
    def __init__(self):
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]

        curr.children['\\'] = TrieNode()
        

    def search(self, word: str) -> bool:

        def searchHelper(word, curr):

            for i, char in enumerate(word):
                if char != '.':
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

                else:
                    for c in curr.children:
                        if searchHelper(word[i + 1:], curr.children[c]):
                            return True

                    return False


            return '\\' in curr.children

        return searchHelper(word, self.root)
        
