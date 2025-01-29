class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res=[]

        for v,c in nums1.items():
            if v in nums2:
                for i in range(min(c,nums2[v])):
                    res.append(v)

        return res