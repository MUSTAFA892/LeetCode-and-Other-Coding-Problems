class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        
        if num <= 1:
            return num

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return mid
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
            
        return False