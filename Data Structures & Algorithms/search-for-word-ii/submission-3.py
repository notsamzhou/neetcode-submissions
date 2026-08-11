class TrieNode:
    def __init__(self):
        self.children = {}
        self.finished = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.finished = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        M, N = len(board), len(board[0])
        visit = set()
        res = []
        def dfs(r, c, node, word):
            if (not 0 <= r < M or not 0 <= c < N or board[r][c] not in node.children
            or (r, c) in visit):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.finished:
                node.finished = False
                res.append(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(M):
            for c in range(N):
                dfs(r, c, root,"")

        return res
