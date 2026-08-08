class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()


        l = 0
        r = 0
        matches = 0
        
        res = float('inf')
        string = [0, 0]

        while l < len(s):
            if s[l] not in target:
                l += 1
                continue


            if r < l:
                r = l

            while r < len(s) and matches != len(target):
                if s[r] in target:
                    window[s[r]] += 1
                    if window[s[r]] == target[s[r]]:
                        matches += 1


                r += 1

        
            while l < r:

                if s[l] in target:
                    
                    
                    if matches == len(target):
                        if r - l  < res:
                            res = r - l 
                            string = [l, r]

                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        matches -= 1
                        l += 1
                        break

                l += 1

            

        return s[string[0]:string[1]]



                



        