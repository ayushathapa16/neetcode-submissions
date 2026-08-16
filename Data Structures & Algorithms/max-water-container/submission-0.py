class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            w = j - i
            if heights[j] > heights[i]:
                h = heights[i]
                i += 1
            else:
                h = heights[j]
                j -= 1
            max_area = max(max_area, h * w)
        return max_area

        