class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        max_ = max_freq

        for i in freq.values():

            if max_freq == i:
                max_ += i

        return max_ - max_freq
                
