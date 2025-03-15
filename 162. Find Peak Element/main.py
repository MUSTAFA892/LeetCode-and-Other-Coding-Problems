class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        greater = max(nums)
        return nums.index(greater)