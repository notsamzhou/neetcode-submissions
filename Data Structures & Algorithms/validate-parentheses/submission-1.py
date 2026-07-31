class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char in ['(', '{',  '[',]:
                stack.append(char)

            elif char in [')',  '}', ']']:
                if not stack:
                    return False

                last = stack.pop()

                if last == '(' and char != ')' or last == '[' and char != ']' or last == '{' and char != '}':
                    return False

            
        if stack:
            return False

        return True


        