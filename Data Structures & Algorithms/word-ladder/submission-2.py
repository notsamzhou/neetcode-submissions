class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        queue = deque([beginWord])


        res = 0
        while queue:
            res += 1

            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1):
                        if chr(c) == word[i]:
                            continue

                        neighbor = word[:i] + chr(c) + word[i + 1:]
                        if neighbor in words:
                            queue.append(neighbor)
                            words.remove(neighbor)

        return 0