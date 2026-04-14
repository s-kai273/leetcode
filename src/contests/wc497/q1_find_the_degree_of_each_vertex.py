class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        answer = []
        for m in matrix:
            answer.append(sum(m))
        return answer
