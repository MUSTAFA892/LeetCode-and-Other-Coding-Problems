class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if bin(nums[i])[-1] != '0':
                for j in range(1,nums[i]+1):
                    sum_ = j-1 | j
                    if sum_ == nums[i]:
                        ans.append(j-1)
                        break
            else:
                ans.append(-1)

        return ans