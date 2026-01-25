class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        l , r = 0, len(nums) - 1
        max_ = 0

        while l <= r:

            min_max_pair = nums[l] + nums[r]
            max_ = max(min_max_pair,max_)

            l += 1
            r -= 1
            

        return max_