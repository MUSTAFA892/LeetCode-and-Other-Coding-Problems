class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                a += 1
                max_ones = max(max_ones, a)
            else:
                a = 0
        
        return max_ones
