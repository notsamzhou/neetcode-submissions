class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        count = {"R": 0, "D": 0}

        for i in range(len(senate)):
            count[senate[i]] += 1

        bans = {"R": 0, "D": 0}

        queue = deque([i for i in range(len(senate))])

        while queue:
            senator = queue.popleft()
            print(senate[senator])

            if bans[senate[senator]] != 0:
                bans[senate[senator]] -= 1
                count[senate[senator]] -= 1
                continue

            if senate[senator] == "R":
                if count["D"] == 0:
                    return "Radiant"
                bans["D"] += 1

            if senate[senator] == "D":
                if count["R"] == 0:
                    return "Dire"
                bans["R"] += 1

            queue.append(senator)




