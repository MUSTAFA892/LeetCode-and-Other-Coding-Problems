class Solution:
    def rotatedDigits(self, n: int) -> int:

        good = {2,5,6,9}
        forbidden = {3,4,7}

        count = 0

        for i in range(2,n+1):
            digit_list = list(map(int, str(i)))
            
            forb = any(d in forbidden for d in digit_list)
            
            if not forb:
                good_any = any(d in good for d in digit_list)

                if good_any:
                        count += 1
                
                
        return count
