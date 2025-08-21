class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_pair = []
        count = 0
        for i in nums:
            if i == 0:
                count += 1
                zero_pair.append(count)

            else:
                count = 0

        return sum(zero_pair)