class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in range(len(asteroids)):

            curr = asteroids[i]

            while stack and curr < 0 and stack[-1] > 0:

                prev = stack.pop()

                if abs(prev) == abs(curr):
                    curr = None
                    break

                if abs(prev) > abs(curr):
                    curr = prev
                    break

                if abs(prev) < abs(curr):
                    continue

            
            if curr:
                stack.append(curr)

        return stack
        