class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max = 0
        while l < r:
            lHeight, rHeight = heights[l], heights[r]
            volume = min(lHeight, rHeight) * (r - l)
            max = volume if volume > max else max
            if lHeight <= rHeight:
                l += 1
            else:
                r -= 1
        return max

        