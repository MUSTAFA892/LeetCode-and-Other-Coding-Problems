class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n
        ans = []

        for i in range(1,n):
            prefix[i] = prefix[i-1]
            if nums[i-1] % 2 == nums[i] % 2:
                prefix[i] += 1
            
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]

            count = prefix[right] - prefix[left]
            if count < 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans