class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        balance = defaultdict(int)

        for frm, to, amount in transactions:
            balance[frm] -= amount
            balance[to] += amount

        debts = [x for x in balance.values() if x != 0]

        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1

            if start == len(debts):
                return 0

            ans = float('inf')

            for i in range(start + 1, len(debts)):
                if debts[start] * debts[i] < 0:
                    debts[i] += debts[start]

                    ans = min(ans, 1 + dfs(start + 1))

                    debts[i] -= debts[start]

            return ans

        return dfs(0)