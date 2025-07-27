class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique_nums = []
        if nums[0]:
            unique_nums.append(nums[0])
        else:
            return 0
        for i in nums:
            if unique_nums[-1] != i:
                unique_nums.append(i)

        count = 0

        for i in range (1,len(unique_nums)-1):
            if unique_nums[i] > unique_nums[i-1] and unique_nums[i] > unique_nums[i+1]:
                count += 1
            elif unique_nums[i] < unique_nums[i-1] and unique_nums[i] < unique_nums[i+1]:
                count += 1
                
            else:
                continue
        return count