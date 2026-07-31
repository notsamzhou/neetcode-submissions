class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]
        offset = 1
        offset_count = 0

        for i in range(1, n+ 1):
            res.append(res[i - offset] + 1)

            offset_count += 1
            if offset_count == offset:
                offset_count = 0
                offset *= 2

        return res
        