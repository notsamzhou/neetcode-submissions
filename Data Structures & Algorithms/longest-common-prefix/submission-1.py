class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

    def lcp(self, word, candidate_prefix_len):
        node = self.root

        for i in range(min(len(word), candidate_prefix_len)):
            if word[i] not in node.children:
                return i

            node = node.children[word[i]]

        return min(len(word), candidate_prefix_len)



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        shortest = 0
        for i in range(1, len(strs)):
            if len(strs[shortest]) > len(strs[i]):
                shortest = i


        trie = Trie()

        trie.insert(strs[shortest])
        candidate_prefix_len = len(strs[shortest])

        for i in range(len(strs)):
            candidate_prefix_len = trie.lcp(strs[i], candidate_prefix_len)

        return strs[0][:candidate_prefix_len]
        