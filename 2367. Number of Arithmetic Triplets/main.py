class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0

        for i in range(1, len(nums)+1):
            for j in range(1, len(nums)+1):
                for k in range(1 , len(nums)+1):
                    if i < j < k:
                        if (
                            nums[j-1] - nums[i-1] == diff
                            and nums[k-1] - nums[j-1] == diff
                        ):
                            count += 1
                        

        return count