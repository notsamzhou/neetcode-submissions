class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(i):

            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):
                sides[side] += matchsticks[i]

                if sides[side] > total // 4:
                    sides[side] -= matchsticks[i]
                    continue

                if backtrack(i + 1):
                    return True

                sides[side] -= matchsticks[i]


            return False

        return backtrack(0)
        