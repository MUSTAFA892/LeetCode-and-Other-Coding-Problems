class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l , r = 1 , 2
        even_count = 0 

        while l <= len(nums)-1:
            left_count = sum(nums[0:l])
            right_count = sum(nums[r-1:len(nums)])
            
            if (left_count - right_count) % 2 == 0:
                even_count += 1
            
            l += 1
            r += 1

        return even_count
    
