class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles
       
        while empty >= numExchange:
            left_over = empty - numExchange
            drank += 1 
            empty  = left_over + 1
            numExchange += 1

        return drank