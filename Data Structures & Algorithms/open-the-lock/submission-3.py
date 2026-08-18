class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = set(deadends)

        queue = deque([("0000", 0)])
        visited.add("0000")

        while queue:

            value, turns = queue.popleft()

            for i in range(4):
                
                num = value[i]

                for diff in [-1, 1]:

                    new = int(num) + diff
                    if new == 10:
                        new = 0

                    if new == -1:
                        new = 9

                    neighbor = value[:i] + str(new) + value[i + 1:]

                    if neighbor == target:
                        return turns + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))

        return -1

        