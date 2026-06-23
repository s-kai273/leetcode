class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        count_list = [0] * len(temperatures)
        stack = list()
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                count_list[j] = i - j
            stack.append(i)
        return count_list
