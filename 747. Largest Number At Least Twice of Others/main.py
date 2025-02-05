class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ = max(nums)
        flag = True
        for i in range(len(nums)):
            if nums[i] == max_:
                continue
            else:
                if max_ < 2 * nums[i]:
                    flag = False
                    break
                    
        if flag:
            return nums.index(max_)
        else:
            return -1
            