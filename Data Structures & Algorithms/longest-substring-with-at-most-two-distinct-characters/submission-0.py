class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        zeros = 26
        counts = defaultdict(int)
        l = 0

        res = 0

        for r in range(len(s)):

            if counts[s[r]] == 0:
                zeros -= 1

            counts[s[r]] += 1


            while zeros < 24:
                counts[s[l]] -= 1

                if counts[s[l]] == 0:
                    zeros += 1

                l += 1

            res = max(res, r - l + 1)

        return res
        
        