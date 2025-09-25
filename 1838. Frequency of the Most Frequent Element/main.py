class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        total = 0
        max_freq = 0
        nums.sort()

        for right in range(len(nums)):
            total += nums[right]
            ops = (nums[right] * (right - left + 1)) - total

            if ops > k:
                total -= nums[left]
                left += 1

            max_freq = max(max_freq , (right - left + 1))

        return max_freq