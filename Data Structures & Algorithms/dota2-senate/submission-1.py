class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        

        count = 0
        bans = {"R": 0, "D": 0}

        queue = deque([i for i in range(len(senate))])

        while queue:
            senator = queue.popleft()


            if bans[senate[senator]] != 0:
                bans[senate[senator]] -= 1
                count = 0
                continue

            if senate[senator] == "R":
                bans["D"] += 1

            if senate[senator] == "D":
                bans["R"] += 1

            if count == len(queue):
                if senate[senator] == "R":
                    return "Radiant"

                if senate[senator] == "D":
                    return "Dire"

            count += 1

            queue.append(senator)