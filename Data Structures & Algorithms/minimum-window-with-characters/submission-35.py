class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = Counter(t)
        window = Counter()


        l = 0
        matches = 0
        
        res = float('inf')
        string = [0, 0]

        for r, char in enumerate(s):
            if s[r] in target:
                window[s[r]] += 1
                if window[s[r]] == target[s[r]]:
                    matches += 1


            while matches == len(target):

                if r - l + 1 < res:
                    res, string = r - l + 1, [l, r+1]

                if s[l] in target:
                    window[s[l]] -= 1

                    if window[s[l]] < target[s[l]]:
                        matches -= 1

                l += 1

                while l <= r and s[l] not in target:
                    l += 1

                
                    
        return s[string[0]:string[1]]