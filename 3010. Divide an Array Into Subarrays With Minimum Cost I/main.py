class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        nums[1:] = sorted(nums[1:])

        return nums[0] + nums[1] + nums[2]
        
"""        min_sum = float('inf')

        for i in range(1,len(nums)-1):
            for j in range(i+1,len(nums)):
                sum_ = nums[0] + nums[i] + nums[j]
                
                min_sum = min(min_sum, sum_)
                

        return min_sum"""