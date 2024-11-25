class Solution:
    def isHappy(self, n: int) -> bool:
        result = set()

        while n != 1:

            if n in result:
                return False
            result.add(n)

            sum_squares = 0
            
            for i in str(n):
                sum_squares += int(i) ** 2
            n = sum_squares
        
        return True