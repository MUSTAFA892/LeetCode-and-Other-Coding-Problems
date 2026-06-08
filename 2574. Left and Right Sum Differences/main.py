class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr = []
        left_sum = []
        right_sum = []
        total_sum = sum(nums)
        left , right = total_sum, total_sum
        n = len(nums)

        for i in range(len(nums)):
            
            left -= nums[n-1-i]
            right -= nums[i]
            
            left_sum.append(left)
            right_sum.append(right)

        for i in range(len(nums)):
            arr.append(abs(right_sum[i] - left_sum[n-1-i]))\
            

        return arr