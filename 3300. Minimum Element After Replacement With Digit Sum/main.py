class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')

        for i in range(len(nums)):
            sum_ = 0
            for j in str(nums[i]):
            
                sum_ += int(j)
                
            min_sum = min(min_sum,sum_)

        return min_sum