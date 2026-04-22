class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0

        l , r = 0 , 0

        while l < len(nums1) and r < len(nums2):

            if nums1[l] <=  nums2[r]:
                max_distance = max(max_distance, r-l)
                r += 1
            
            else:
                l += 1
                if l > r:
                    r = l 

        return max_distance