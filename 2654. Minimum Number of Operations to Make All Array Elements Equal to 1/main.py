class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if 1 in nums:
            return n - nums.count(1)
        
        min_len = float('inf')
        for i in range(n):
            gcd_val = nums[i]
            for j in range(i+1, n):
                gcd_val = math.gcd(gcd_val, nums[j])
                if gcd_val == 1:
                    min_len = min(min_len, j - i + 1)
                    break  
        
        if min_len == float('inf'):
            return -1
        
        return (min_len - 1) + (n - 1)
