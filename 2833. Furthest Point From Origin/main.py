class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L_occ = moves.count('L')
        R_occ = moves.count('R')
        change = 0
        if L_occ > R_occ:
            change = -1
        else:
            change = 1

        count = 0
        for i in moves:
            if i == 'L' or (i == '_' and change == -1) :
                count -= 1
            else:
                count += 1

        return abs(count) 