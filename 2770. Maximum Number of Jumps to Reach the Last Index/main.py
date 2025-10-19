class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * (len(nums) - 1)
        dp.insert(0,0)

        for i in range(1,len(nums)):
            for j in range(0,i):
                sub = nums[i] - nums[j]
                if -target <= sub <= target and dp[j] != -1:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return dp[-1]