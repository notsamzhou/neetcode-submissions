class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        starts = dict()
        for i, char in enumerate(s):
            if char not in starts:
                starts[char] = i


        res = 0
        for char in starts:
            l = 0
            r = 0
            k_rem = k
            while r < len(s):
                if s[r] != char:
                    k_rem -= 1

                    if k_rem < 0:
                        while s[l] == char:
                            l += 1

                        l += 1
                        k_rem = 0
                res = max(res, r - l + 1)

                r += 1

        return res

                