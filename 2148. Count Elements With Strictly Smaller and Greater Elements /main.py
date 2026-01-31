class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            small = 0
            large = 0
            sample_arr = [n for n in nums if n != nums[i]]
            for j in sample_arr:
                end = 0

                if nums[i] <= j and small != 1:
                    small += 1
                    end += 1   
                    
                if nums[i] >= j and large != 1:
                    large += 1
                    end += 1
                    
                if end == 2:
                    break
                    
            if small == 1 and large == 1:
                count += 1
            
        return count