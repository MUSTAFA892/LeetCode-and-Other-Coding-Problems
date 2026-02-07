class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_size = 0
        l = 0

        for r in range(len(nums)):

            while l <= r and nums[r] > nums[l] * k:
                l += 1
            
            max_size = max(max_size, r - l + 1)

        return len(nums) - max_size
        
"""        nums.sort()
        max_size = 0

        l, r = 0, 0

        while r < len(nums):
            window = nums[l:r+1]
            max_window = nums[r]
            min_window = nums[l]
            
            if max_window <= (min_window * k) :
                max_size = max(max_size, len(window))
                r += 1
                
            else:
                l += 1
                r = l

        return len(nums) - max_size"""