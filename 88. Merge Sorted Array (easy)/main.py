class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Let us deal with this problem with the pointer approach
        t1 = m - 1 # Track of the elements m in nums1
        t2 = n - 1 # Track of the elements n in nums2
        t = m + n - 1 #Track of the total elemnets of nums1

        while t2>=0: # Run the loop until the elements of nums2 is empty 
            if t1>=0 and nums1[t1] > nums2[t2]: #if the elements if elements of nums1 is > than the elements of nums2
                nums1[t] = nums1[t1] # Replace the element of the nums1(t) with the nums1(t1)
                t1-=1 # Decrement one in the track of nums1
            else:
                nums1[t] = nums2[t2] # Replace nums1(t) with the nums2(t2)
                t2-=1 # Decrement one in the track of nums1
            t-=1 # Decrement one in the track of the total elements of nums1






"""     ALSO  YOU CAN GO WITH THIS APPROACH TOO
        n = len(nums1) - m
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()"""