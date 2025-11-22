class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        gap = 0
        previous_index = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                
                if previous_index == -1:
                    previous_index = i
                    continue

                gap = i - previous_index - 1
                if gap >= k:
                    previous_index = i
                    continue
                else:
                    return False
                
        return True