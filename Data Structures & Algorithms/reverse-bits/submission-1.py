class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        for i in range(32):
            newBit = (n & 1)
            n >>= 1
            res += (newBit << (31 - i))
            

        return res
        