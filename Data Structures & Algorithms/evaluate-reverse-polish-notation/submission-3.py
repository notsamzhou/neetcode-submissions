class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in "+-*/":
                token = int(token)
                stack.append(token)

            else:
                op = token
                second = stack.pop()
                first = stack.pop()

                if op == "+":
                    stack.append(first + second)
                if op == '-':
                    stack.append(first - second)
                if op == '*':
                    stack.append(first * second)
                if op == '/':
                    stack.append(int(first / second))

        return stack[0]

        