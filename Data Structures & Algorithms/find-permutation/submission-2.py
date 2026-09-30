class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        res = []

        for i in range(1, len(s)+1):
            if s[i-1] == 'I':
                stack.append(i)
                while stack:
                    res.append(stack.pop())

                
            else:
                stack.append(i)

        stack.append(len(s)+1)
        while stack:
            res.append(stack.pop())
        
        return res