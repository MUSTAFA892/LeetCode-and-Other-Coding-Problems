class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_low , pointer_high = 0, len(height) - 1  
        max_area = 0
        while pointer_low < pointer_high:
            width = pointer_high - pointer_low # Getting the width
            area = min(height[pointer_high],height[pointer_low]) * width # height and area calculate
            max_area = max(max_area, area)  # max area between the width and height
            if height[pointer_low] < height[pointer_high]:
                pointer_low += 1
            
            else:
                pointer_high -= 1
            
        return max_area

 