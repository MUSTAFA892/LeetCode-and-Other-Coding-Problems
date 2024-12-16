class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        count = 0
        while count != k:
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
            count += 1
        return nums