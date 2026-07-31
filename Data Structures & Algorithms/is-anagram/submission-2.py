class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        chars = dict()
        for char in s:
            if char not in chars:
                chars[char] = 0

            chars[char] += 1

        for char in t:
            if char not in chars:
                return False
            chars[char] -= 1

        for key in chars:
            if chars[key] != 0:
                return False

        return True
        