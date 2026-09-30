class Solution:
    def findPermutation(self, s: str) -> List[int]:
        
        def reverse(res, j, i):

            while j < i:
                temp = res[j]

                res[j] = res[i]
                res[i] = temp

                i -= 1
                j += 1

        res = [i for i in range(1, len(s) + 2)]
        i = 0

        while i < len(s):
             
            j = i

            while i < len(s) and s[i] == 'D':
                i += 1

            reverse(res, j, i)

            i += 1

        return res

