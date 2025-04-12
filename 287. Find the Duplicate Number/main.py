class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = [0] * len(nums)

        for i in nums:
            if ans[i] == 1:
                return i
            ans[i] = 1

"""        freq = Counter(nums)

        for val , count in freq.items():
            if count >= 2:
                return val"""