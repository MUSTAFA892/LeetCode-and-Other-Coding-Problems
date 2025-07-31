class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        odd_idx = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr.append(nums[i])
            else:
                odd_idx.append(nums[i])

    
        return arr + odd_idx