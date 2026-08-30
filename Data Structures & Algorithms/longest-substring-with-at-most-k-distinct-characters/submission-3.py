class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        counts = defaultdict(int)
        zeros = 26

        res = 0
        l = 0
        for r in range(len(s)):


            if counts[s[r]] == 0:
                zeros -= 1

            counts[s[r]] += 1


            while 26 - zeros > k:
                
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    zeros += 1
                l += 1



            res = max(res, r - l + 1)
        return res