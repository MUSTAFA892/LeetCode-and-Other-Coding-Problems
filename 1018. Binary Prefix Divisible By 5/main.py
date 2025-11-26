class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        rem = 0

        for i in range(len(nums)):
            rem = (rem * 2 + nums[i]) % 5

            if rem == 0:
                ans.append(True)
            else:
                ans.append(False)

            
        return ans