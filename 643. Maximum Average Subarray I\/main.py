class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        ans = [current_sum/k]

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            ans.append(current_sum/k)

        return max(ans)
"""        l , r = 0 , k
        ans = []

        while r <= len(nums):
            sum_ = sum(nums[l:r]) / k
            ans.append(sum_)
            l+=1
            r+=1

        return max(ans)"""