class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        i = len(digits) - 1

        carry = digits[-1] == 10
        while carry and i > 0:
            digits[i] = 0

            i -= 1
            digits[i] += 1
            carry = digits[i] == 10

        if carry:
            digits[0] = 0
            digits = [1] + digits

        return digits

            
            
        