class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        count = [0] * (n + 1)

        for a, b in trust:
            count[a] = n
            count[b] += 1


        judge = None

        for i in range(1, n + 1):

            if count[i] == n - 1:
                if judge is not None:
                    return -1
                judge = i

        return judge if judge is not None else -1

        