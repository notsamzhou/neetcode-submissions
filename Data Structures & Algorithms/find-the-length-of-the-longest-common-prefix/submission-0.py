class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()

        # Insert all numbers from arr1 into the trie
        for num in arr1:
            node = root
            for digit in str(num):
                if digit not in node.children:
                    node.children[digit] = TrieNode()
                node = node.children[digit]

        # Find the longest matching prefix for each number in arr2
        answer = 0

        for num in arr2:
            node = root
            length = 0

            for digit in str(num):
                if digit not in node.children:
                    break
                node = node.children[digit]
                length += 1

            answer = max(answer, length)

        return answer