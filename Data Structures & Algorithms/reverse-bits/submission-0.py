class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        for i in range(32):
            newBit = n % 2
            n >>= 1

            res <<= 1
            res += newBit
            

        return res
        