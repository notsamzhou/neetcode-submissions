class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: (-x[0], x[1]))


        res = 0
        stack = []
        for car in cars:

            time1 = (target - car[0]) / car[1]
            # if we catch up to a slower car ahead of us, ignore the faster car
            if stack and stack[-1] >= time1:
                continue

            stack.append(time1)

        return len(stack)

