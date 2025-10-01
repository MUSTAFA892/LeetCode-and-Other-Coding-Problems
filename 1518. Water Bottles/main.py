class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles

        while empty >= numExchange:
            fullBottle = empty // numExchange
            empty = abs((numExchange * fullBottle) - empty)
            drank += fullBottle
            empty += fullBottle

        return drank