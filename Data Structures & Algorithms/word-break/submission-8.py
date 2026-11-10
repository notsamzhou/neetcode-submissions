class TrieNode:
    def __init__(self):
        self.children = dict()
        self.finished = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        longest = 0
        root = TrieNode()
        for word in wordDict:
            curr = root
            longest = max(longest, len(word))
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.finished = True

        cache = {}
        def dp(i):

            if i == len(s):
                return True

            if i in cache:
                return cache[i]


            curr = root
            for j in range(longest):
                if i+j >= len(s) or s[i+j] not in curr.children:
                    break

                curr = curr.children[s[i+j]]

                if curr.finished:
                    if dp(i+j+1):
                        cache[i] = True
                        return cache[i]

            cache[i] = False

            return False

        

        dp(0)
        print(cache)
        return cache[0]
