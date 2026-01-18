class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum_ = math.prod(nums)
        result = nums.copy()
        zero_idx = 0
        zero_count = 0
        ok = False

        prod = 1
        for i in range(len(nums)):
            if result[i] == 0:
                if not ok:
                    zero_idx = nums.index(0)
                    zero_count = nums.count(0)
                    ok = True
                result[i] = 0
            else:
                prod *= result[i]
                result[i] = sum_ // result[i]
            
        if zero_count == 1:
            result[zero_idx] = prod
            
        return result
        
"""        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result"""