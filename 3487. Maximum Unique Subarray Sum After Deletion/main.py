from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        max_sum = 0

        for num in set(nums):
            if num > 0:
                max_sum += num
        
        if max_sum:
            return max_sum
        
        else:
            return max(nums)



"""        seen = []

        for i in range(len(nums)):
            number = abs(nums[i])
            if number in  seen:
                seen.remove(number)
            seen.append(number)

        return sum(seen)"""

"""        left = 0 
        max_sum = 0
        current_sum = 0

        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum"""