class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        sum_  = 0
        max_operations = -1
        target = sum(nums) - x

        if target < 0 :
            return -1

        for right in range(len(nums)):
            sum_ += nums[right]

            while sum_ > target and left <= right :

                sum_ -= nums[left]

                left += 1
            
            if sum_ == target:    
                max_operations = max(max_operations, right - left + 1)
        
        if max_operations == -1:
            return -1
        
        return len(nums) - max_operations