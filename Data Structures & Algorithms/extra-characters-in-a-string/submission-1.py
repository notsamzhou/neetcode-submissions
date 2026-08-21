class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.finished = False

            def addWord(self, word):
                curr = self

                for char in word:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()

                    curr = curr.children[char]

                curr.finished = True


            def findWord(self, word):
                curr = self

                for char in word:
                    if char not in curr.children:
                        return False

                    curr = curr.children[char]

                return curr.finished

        trie = TrieNode()
        for word in dictionary:
            trie.addWord(word)

        # dp[i] = minimum over the range i to j
        cache = {}
        def dp(i):

            if i == len(s):
                return 0

            if i in cache:
                return cache[i]

            res = 1 + dp(i + 1)
            for j in range(i, len(s)):
                if trie.findWord(s[i:j + 1]):
                    res = min(res, dp(j + 1))

            cache[i] = res
            return res

        return dp(0)
