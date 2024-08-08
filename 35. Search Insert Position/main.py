class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first,last = 0, (len(nums)) - 1
        while first <= last:
            mid = (first + last) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid +1
        return first