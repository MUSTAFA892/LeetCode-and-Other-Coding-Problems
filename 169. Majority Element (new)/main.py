class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums)//2]
        
"""        freq = Counter(nums)
        max_  = 0
        ans = 0

        for val , count in freq.items():
            if max_  < count:
                ans = val 
                max_ = count
            
        return ans"""
        