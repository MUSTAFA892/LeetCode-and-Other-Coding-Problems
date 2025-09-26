from itertools import combinations
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(n-1,1,-1):

            i,j = 0 , k-1

            while i<j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i)
                    j -= 1 
                    
                else:
                    i += 1
        return count 
                
"""        nums.sort()
        combo = list(combinations(nums,3))
        count = 0
        for sort in combo:
            if sort[0] + sort[1] > sort[2]:
                count += 1
                
        return count"""