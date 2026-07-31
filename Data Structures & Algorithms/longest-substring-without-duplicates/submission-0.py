class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        seen = set()

        l = 0
        r = 0
        while r < len(s):

            if s[r] in seen:

                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1

                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            res = max(r - l + 1, res)
            r += 1

            print(l, r, seen)

        return res


        