class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:
            return -1

        excess = [gas[i] - cost[i] for i in range(len(gas))]
        remaining = 0
        res = 0
        for i in range(len(gas)):
            remaining += excess[i]
            if remaining < 0:
                res = i + 1
                remaining = 0

        return res
        