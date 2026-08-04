class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = Counter()
        
        l = 0
        for r, char in enumerate(s2):
            if r >= len(s1):
                window[s2[l]] -= 1
                l += 1

            window[s2[r]] += 1

            if window == target:
                return True


        return False

            