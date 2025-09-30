class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
    
            for i in range(1,len(nums)):
                sums = (nums[i-1] + nums[i]) % 10
                nums[i-1] = sums
                
            nums.pop()
            
        return nums[0]