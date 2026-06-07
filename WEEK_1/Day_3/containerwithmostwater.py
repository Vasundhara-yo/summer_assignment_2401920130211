class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = float('-inf')

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            
            # Move the pointer with the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
