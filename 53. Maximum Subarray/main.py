class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        res = nums[0]

        for i in range(len(nums)):
            max_sum += nums[i]
            
            if max_sum > res:
                res = max_sum

            if max_sum < 0:
                max_sum = 0

        return res