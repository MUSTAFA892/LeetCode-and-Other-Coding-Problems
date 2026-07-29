class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro = (nums[i] - 1) * (nums[j] - 1)
                max_pro = max(max_pro, pro)
        
        return max_pro