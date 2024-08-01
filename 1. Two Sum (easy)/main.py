class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Let us go with the two pointer approach
        nums = sorted(enumerate(nums), key=lambda x: x[1])  # Sort the array along with original indices
        left, right = 0, len(nums) - 1 #Store the elements in left and right 
        while left < right: #run the loop
            current_sum = nums[left][1] + nums[right][1] # check the current sum of two pointer
            if current_sum == target: # if its equal return index
                return [nums[left][0], nums[right][0]]
            elif current_sum < target: # is sum is lesser than target add 1 in left
                left += 1
            else:
                right -= 1 #subtract 1 in right
        return []

        """or you can go with the brute force approach
        for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
        """