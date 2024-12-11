class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        l , r = 0 , 0
        while r < n:
            if (nums[r] - nums[l] >  2 * k):
                l += 1
            ans = max(ans , r-l+1)
            r += 1
        return ans