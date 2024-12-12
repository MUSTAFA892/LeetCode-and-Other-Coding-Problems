class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        perm = itertools.permutations(nums)
        for i in perm:
            if i not in result:
                result.append(i)
        return result