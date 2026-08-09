class Solution:
    def countSubstrings(self, s: str) -> int:
        


        
        res = 0

        for c in range(len(s)):
            res += 1

            low = c - 1
            high = c + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                res += 1
                low -= 1
                high += 1


            low = c
            high = c + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                res += 1
                low -= 1
                high += 1


        return res
            