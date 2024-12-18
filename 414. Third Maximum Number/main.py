class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        sorted_nums = sorted(nums, reverse=True)
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        else:
            return sorted_nums[0]