class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: -x[0])

        stack = []
        for car in cars:

            timeToDest = (target - car[0]) / car[1]

            if stack and stack[-1] >= timeToDest:
                continue

            stack.append(timeToDest)

        return len(stack)