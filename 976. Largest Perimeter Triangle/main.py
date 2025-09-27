class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        for i in range(len(nums)-2):
        
            if nums[i+2] + nums[i+1] > nums[i]:
                perimeter = max(perimeter, nums[i] + nums[i+1] + nums[i+2])
        
        return perimeter