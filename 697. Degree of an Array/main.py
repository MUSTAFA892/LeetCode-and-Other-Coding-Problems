class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_fre = max(freq.values())

        first_idx = {}
        last_idx = {}

        for i, num in enumerate(nums):
            if num not in first_idx:
                first_idx[num] = i
            last_idx[num] = i 

        min_length = len(nums) + 1

        for num in freq:
            if freq[num] == max_fre:
                length = last_idx[num] - first_idx[num] + 1
                min_length = min(min_length , length)

        return min_length