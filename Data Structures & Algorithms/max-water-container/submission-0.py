class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                height = min([heights[i], heights[j]])
                area = width * height
                if area > max_water:
                    max_water = area
        return max_water