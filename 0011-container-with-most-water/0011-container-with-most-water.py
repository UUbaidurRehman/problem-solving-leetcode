class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            height_r = min(height[l], height[r])
            width_r = r-l
            area = height_r * width_r
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
           
        return max_area
            
            
