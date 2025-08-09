class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 3:
            return False
        else:
            while n % 2 == 0:
                n /= 4
            
            if n == 1:
                return True
            else:
                return False