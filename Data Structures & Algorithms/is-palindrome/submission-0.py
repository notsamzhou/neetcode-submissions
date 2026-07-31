class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s) - 1

        while l < r:
            if not (ord('a') <= ord(s[l]) <= ord('z') or ord('0') <= ord(s[l]) <= ord('9')):
                l += 1
                continue
            if not (ord('a') <= ord(s[r]) <= ord('z') or ord('0') <= ord(s[r]) <= ord('9')):
                r -= 1
                continue
                

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True

        