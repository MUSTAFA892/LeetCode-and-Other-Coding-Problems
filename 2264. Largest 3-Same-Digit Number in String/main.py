class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        unique_nums = []

        for i in range(1,len(num)):
            if num[i-1] == num[i]:
                count += 1
            else:
                count = 1
            if count == 3:
                count = 1
                unique_nums.append(num[i-1])
        if len(unique_nums) > 0:
            max_nums = max(unique_nums)
            return max_nums * 3
        else:
            return ""