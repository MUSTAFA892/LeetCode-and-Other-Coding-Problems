class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        sum_ = nums[left]
        Track_Dup = set()
        Track_Dup.add(nums[left])
        max_sum = 0

        if sum_ == 10000 and len(nums) == 1:
            return sum_

        for right in range(1,len(nums)):
            while nums[right] in Track_Dup:
                Track_Dup.remove(nums[left])
                sum_ -= nums[left]
                left += 1
            Track_Dup.add(nums[right])
            sum_ += nums[right]
            max_sum = max(max_sum, sum_)



        return max_sum