class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_ele = max(nums)
        base = []

        for i in range(1,max_ele+1):
            base.append(i)

        base.append(max_ele)

        return base == sorted(nums)