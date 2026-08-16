class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIdx = dict()
        for i, char in enumerate(s):
            if char not in lastIdx:
                lastIdx[char] = i

            lastIdx[char] = i

        i = 0
        start = 0
        end = 0
        res = []
        while i < len(s):

            end = max(lastIdx[s[i]], end)

            if i == end:
                res.append(end - start + 1)
                start = i + 1

            i += 1

        return res


        