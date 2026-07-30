class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        vote1, vote2 = 0, 0

        for num in nums:
            if candidate1 == num:
                vote1 += 1
            elif candidate2 == num:
                vote2 += 1
            elif vote1 == 0:
                candidate1 = num
                vote1 = 1
            elif vote2 == 0:
                candidate2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1

        result = []

        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result