class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        
        used = dict()
        ref = Counter(s1)
        matches = 0

        for r in range(len(s2)):
            used[s2[r]] = used.get(s2[r], 0) + 1

            if used[s2[r]] == ref[s2[r]]:
                matches += 1

                if matches == len(ref):
                    return True

            elif ref[s2[r]] == 0:
                while l <= r:
                    used[s2[l]] -= 1
                    l += 1
                matches = 0

            elif used[s2[r]] > ref[s2[r]]:
                while s2[l] != s2[r]:
                    if used[s2[l]] == ref[s2[l]]:
                        matches -= 1

                    used[s2[l]] -= 1
                    l += 1

                used[s2[l]] -= 1
                l += 1


        return False

            


        