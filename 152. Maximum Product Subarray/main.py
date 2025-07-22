class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = nums[0]
        min_pro = nums[0]
        result =  nums[0]

        if len(nums) > 1:

            for i in range (1,len(nums)):
                product = nums[i] , nums[i] * max_pro , nums[i] * min_pro

                max_pro = max(product)
                min_pro = min(product)
                result = max(result,max_pro)

            return result

        else:
            
            return result 

    