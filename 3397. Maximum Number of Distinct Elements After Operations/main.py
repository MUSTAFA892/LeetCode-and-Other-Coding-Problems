class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        next_avail = float('-inf')

        for i in range(len(nums)):
            value = max(nums[i]-k,next_avail+1)
            
            if value <= nums[i] + k:
                next_avail = value  
                count += 1
            
        return count
            
"""        arr = []
        nums.sort()

        for i in range(len(nums)):
            range_start = nums[i]-k
            range_end = nums[i]+k

            for j in range(range_start,range_end+1):
                if j not in arr:
                    arr.append(j)
                    break
            
        return len(arr)"""