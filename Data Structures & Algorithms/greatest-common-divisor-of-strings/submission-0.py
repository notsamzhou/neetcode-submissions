class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        res = 0
        for i in range(len(str2)):

            if len(str2) % (i + 1) == 0 and len(str1) % (i + 1) == 0:
                if str2[:i+1] * (len(str1) // (i + 1)) == str1:
                    res = i+1

        return str2[:res]


        
        