class Solution:
    def splitArray(self, nums: List[int]) -> int:      
        first_nums = []
        second_nums = []

        def is_prime(num):
            if num < 2:
                return False
                
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
        for i in range(len(nums)):
            if is_prime(i):
                second_nums.append(nums[i])
            else:
                first_nums.append(nums[i])
            
        return abs(sum(first_nums) - sum(second_nums))
                