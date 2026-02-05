class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
            
                val = i + nums[i]
                if val > len(nums) - 1:
                    val -= len(nums)
                    
                    val %= len(nums)
                result.append(nums[val])
                
            elif nums[i] < 0:
                
                val = i - abs(nums[i])
                if val < 0:
                    
                    val += len(nums)
                    val %= len(nums)
                result.append(nums[val])
                
            else:
                result.append(nums[i])
            
        return result