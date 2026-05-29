class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid
        row = right if matrix[right][0] <= target else left
        left = 0
        right = len(matrix[row]) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if matrix[row][mid] <= target:
                left = mid
            else:
                right = mid
        for val in [matrix[row][left], matrix[row][right]]:
            if val == target:
                return True
        return False
