class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        arr = []
        index_ = []

        n = len(nums)

        curr_idx = [0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr_idx.append(i)
            else:
                arr.append(len(curr_idx))
                index_.append(curr_idx.copy())
                curr_idx = [i]
                
        arr.append(len(curr_idx))
        index_.append(curr_idx.copy())

        max_k = 0
        for i in range(1,len(index_)):
            if index_[i-1][-1] + 1 == index_[i][0]:
                max_k = max(max_k,min(len(index_[i-1]), len(index_[i])))
                
        for length in arr:
            if length//2 > max_k:
                max_k = length//2
                
        return max_k
