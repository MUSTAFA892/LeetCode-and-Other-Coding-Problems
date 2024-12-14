class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        left = 0
        min_ = deque()
        max_ = deque()

        for right in range(n):
            while min_ and nums[min_[-1]] >= nums[right]:
                min_.pop()
            min_.append(right)

            while max_ and nums[max_[-1]] <= nums[right]:
                max_.pop()
            max_.append(right)

            while nums[max_[0]] - nums[min_[0]] > 2:
                left += 1

                if min_[0] < left:
                    min_.popleft()
                if max_[0] < left:
                    max_.popleft()
            
            count += (right - left + 1) 
        return count