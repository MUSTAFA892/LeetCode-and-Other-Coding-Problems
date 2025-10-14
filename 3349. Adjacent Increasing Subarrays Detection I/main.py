class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

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

        for i in range(1,len(index_)):
            if len(index_[i-1]) >= k and len(index_[i]) >= k:
                if index_[i-1][-1] + 1 == index_[i][0]:
                    return True

        for i in range(0, n - 2 * k + 1):
            first = nums[i : i + k]
            second = nums[i + k : i + 2 * k]
            if all(first[j] < first[j + 1] for j in range(k - 1)) and all(second[j] < second[j + 1] for j in range(k - 1)):
                return True
        
        return False