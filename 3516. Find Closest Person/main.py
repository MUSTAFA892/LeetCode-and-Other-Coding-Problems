class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        per_1 = abs(x-z)
        per_2 = abs(y-z)

        if per_1 > per_2:
            return 2
        
        elif per_1 < per_2:
            return 1

        else:
            return 0