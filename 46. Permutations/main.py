import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = itertools.permutations(nums)
        for i in perm:
            result.append(i)
        return result