class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        def helper(m):
            s = 0
            while m:
                s += (m % 10) ** 2
                m = m // 10

            return s

        while True:

            curr = helper(n)
            if curr == 1:
                return True

            if curr in seen:
                return False

            seen.add(curr)
            n = curr


        

            
        