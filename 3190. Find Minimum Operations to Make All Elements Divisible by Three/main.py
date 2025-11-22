class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        alr_zero = 0
        for i in nums:
            if i % 3 == 0:
                alr_zero += 1

        return len(nums) - alr_zero