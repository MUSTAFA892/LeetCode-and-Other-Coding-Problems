class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            current_length = 1

            current_number = num

            while current_number * current_number in nums_set:
                current_number = current_number * current_number
                current_length += 1

            if current_length >= 2:
                max_length = max(max_length , current_length)

        if max_length >= 2:
            return max_length
        else:
            return -1