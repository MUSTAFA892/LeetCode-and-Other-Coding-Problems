import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0 

        for a in range(1,n+1):
            for b in range(1,n+1):
                sum_ = a**2 + b**2
                c = int(math.sqrt(sum_))
                if c * c == sum_ and c <= n:
                    count += 1
                
        return count