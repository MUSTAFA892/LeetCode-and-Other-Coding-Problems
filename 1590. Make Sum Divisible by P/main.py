class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = 0
        total_rem = sum(nums) % p
        if total_rem == 0:
            return 0
        hashp = {0:-1}
        min_len = float('inf')

        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_rem = prefix_sum % p
            sub_arr = (prefix_rem - total_rem) % p
            
            if sub_arr in hashp:

                prev_idx = hashp[sub_arr]
                sub_len = i - prev_idx     

                if sub_len != len(nums):
                    min_len = min(min_len, sub_len)
            
                         
            hashp[prefix_rem] = i

        return -1 if min_len == float('inf') else min_len

        
"""        sum_nums = sum(nums) % p
        min_len = float('inf')

        if sum_nums == 0:
            return 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):

                if i == 0 and j == len(nums):
                    continue

                if sum(nums[i:j]) % p == sum_nums:
                    min_len = min(min_len, j - i)

        if min_len == float('inf'):
            return -1
        else:
            return min_len

"""