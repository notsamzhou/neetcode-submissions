class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        p1 = -1
        p2 = -1

        same = word1 == word2

        res = 10**10

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                if same:
                    p2 = p1
                p1 = i

                if p2 != -1:
                    res = min(res, p1 - p2)

            elif wordsDict[i] == word2:
                p2 = i
                if p1 != -1:
                    res = min(res, p2 - p1)

        return res
