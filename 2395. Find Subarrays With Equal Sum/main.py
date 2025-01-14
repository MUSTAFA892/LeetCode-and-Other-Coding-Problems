class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        repeatation = set()

        for i in range(len(nums) - 1):
            total = nums[i] + nums[i+1]
            if total in repeatation:
                return True
            
            repeatation.add(total)

        return False