class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        countS1 = Counter(s1)

        i = 0
        j = 0

        while countS1 and j < len(s2):
            if s2[j] in countS1:
                countS1[s2[j]] -= 1
                if countS1[s2[j]] == 0:
                    del countS1[s2[j]]
                j += 1

            else:
                while i < j and s2[i] != s2[j]:
                    countS1[s2[i]] = countS1.get(s2[i], 0) + 1
                    i += 1


                j += 1
                i += 1
        
        if countS1:
            return False

        return True

        

        
        