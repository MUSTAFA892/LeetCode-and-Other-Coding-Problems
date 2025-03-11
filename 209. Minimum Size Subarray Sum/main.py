class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        min_len = float('inf')

        for right in range(len(nums)):
            sum_ += nums[right]

            while sum_ >= target:
                min_len = min(min_len, right - left + 1)

                sum_ -= nums[left]

                left += 1
            
        if min_len < float('inf'):
            return min_len
        return 0

"""        ans = []

        left = 0
        right = 0

        while right < len(nums):
            sum_ = sum(nums[left:right+1])
            if sum_ == target:
                ans.append(nums[left:right+1])
                right += 1
            elif sum_ > target:
                left += 1
            else:
                right +=1 

        len_ = []
        for i in ans:
            len_.append(len(i))
        if len_:
            return min(len_)
        else:
            return 0"""