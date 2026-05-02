class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        def initial_ele(nums):
            prod = 0
            for i in range(len(nums)):
                prod += (i*nums[i])
            return prod

        max_val = float('-inf')

        base_sum = initial_ele(nums)
        max_val = max(max_val , base_sum)
        arr_sum = sum(nums)
        n = len(nums)

        for i in range(len(nums)-1,0,-1):
            comp = (base_sum + arr_sum) - (n * nums[i])
            base_sum = comp
            max_val = max(max_val , base_sum)

        return max_val  

"""        max_val = float('-inf')

        for i in range(len(nums)):
            prod = 0
            temp = nums[-1]
            for j in range(len(nums)):
                prod += (j*nums[j])
                
            max_val = max(max_val, prod)
            nums.pop()
            nums.insert(0, temp)

        return max_val"""