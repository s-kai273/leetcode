class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_rec = 0
        for i, h in enumerate(heights):
            start_pos = i - 1
            while stack and stack[-1][0] > h:
                ph, psp = stack.pop()
                rec = ph * ((i - 1) - psp)
                max_rec = max(max_rec, rec)
                start_pos = psp
            stack.append((h, start_pos))
        while stack:
            ph, psp = stack.pop()
            rec = ph * ((len(heights) - 1) - psp)
            max_rec = max(max_rec, rec)
        return max_rec
