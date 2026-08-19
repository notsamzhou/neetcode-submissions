class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        place = {}
        for i, char in enumerate(order):
            place[char] = i

        for i in range(len(words) - 1):
            
            curr = words[i]
            nxt = words[i+1]

            j = 0
            while j < len(curr) and j < len(nxt) and curr[j] == nxt[j]:
                j += 1

            if j == len(curr) and j < len(nxt):
                continue

            if j == len(nxt) and j < len(curr):
                return False


            if place[curr[j]] > place[nxt[j]]:
                return False

        return True

            