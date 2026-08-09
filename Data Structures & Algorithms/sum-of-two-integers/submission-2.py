class Solution:
    def getSum(self, a: int, b: int) -> int:

        res = 0

        for i in range(32):
            digit = 1 << i

            if not (a & digit) and not (b & digit):
                continue


            if (a & digit) and (b & digit):
                res |= (1 << i + 1)

            else:
                if not res & digit:
                    res |= (1 << i)

                else:
                    res &= ~(1 << i)
                    res |= (1 << i + 1)

        MASK = ~(~0 << 32)

        res &= MASK

        if res & (1 << 31):
            res = ~(res ^ MASK)
        return res

                

        