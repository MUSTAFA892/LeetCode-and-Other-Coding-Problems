class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            min_ = nums.index(min(nums))
            nums[min_] = -nums[min_]
        
        return sum(nums)