class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            value = nums2.index(num)
            found_greater = False

            for j in range(value + 1, len(nums2)):
                if nums2[j] > num:
                    result.append(nums2[j])
                    found_greater = True
                    break
        
            if not found_greater:
                result.append(-1)

        return result
