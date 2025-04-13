class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = [0] * (len(nums) + 1)
        ans = []

        for i in nums:
            if temp[i] == 1:
                ans.append(i)
            temp[i] = 1

        for i in range(1,len(nums)+1):
            if temp[i] == 0:
                ans.append(i)
                
        return ans
 