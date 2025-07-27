class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        Total_sum = sum(nums)
        
        final_arr = []


        for i in nums:
            final_arr.append(i)
            
            min_sum = Total_sum - sum(final_arr)

            
            if sum(final_arr) > min_sum:
                break
            else:
                min_sum = 0
                
        return final_arr