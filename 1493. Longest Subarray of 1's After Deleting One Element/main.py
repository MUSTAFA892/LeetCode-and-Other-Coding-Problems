class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , r , max_length , zero = 0 , 0 , 0 , 0

        while r < len(nums):
                if nums[r] == 0:
                    zero += 1

                if zero > 1:
                    while zero > 1:
                        if nums[l] == 0:
                            zero -= 1
                        l += 1

                max_length = max(max_length , r - l)
                r += 1
        
        return max_length