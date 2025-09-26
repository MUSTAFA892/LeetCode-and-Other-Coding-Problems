class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        l , r = 0 , k-1
        min_val = float('inf')

        while r < len(nums):
            difference = nums[r] - nums[l]
            min_val = min(min_val,difference)
            l+=1 
            r+=1

        return min_val
            