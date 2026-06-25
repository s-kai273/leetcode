class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = list()
        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        stack.sort()
        fleet = 0
        while stack:
            fleet += 1
            first = stack.pop()
            dt = (target - first[0]) / first[1]
            while True:
                if (
                    stack
                    and stack[-1][1] > first[1]
                    and (first[0] - stack[-1][0]) / (stack[-1][1] - first[1]) <= dt
                ):
                    stack.pop()
                else:
                    break
        return fleet
