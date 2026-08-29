class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        end_idx = None
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                end_idx = i

        if end_idx is None:
            return 0

        
        neighbors = {}
        for j, word in enumerate(wordList):
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+ 1:]

                if pattern not in neighbors:
                    neighbors[pattern] = []
                neighbors[pattern].append(j)


        queue = deque()

        queue.append((0, -1))


        visited = set()
        while queue:
            dist, word_idx = queue.popleft()


            if word_idx == -1:
                currWord = beginWord

            else:
                currWord = wordList[word_idx]

            if word_idx == end_idx:
                return dist + 1


            for i in range(len(currWord)):
                pattern = currWord[:i] + "*" + currWord[i+1:]

                if pattern in neighbors:

                    for nei in neighbors[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append((dist+1, nei))

        return 0
                    



        
        