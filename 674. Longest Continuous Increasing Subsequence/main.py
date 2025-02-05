class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_ = []


        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1

            else:
                max_.append(count)
                count = 1
        max_.append(count)          
        return max(max_)