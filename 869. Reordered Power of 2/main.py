from itertools import permutations as p
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        permut = []
        start_zero = False

        for i in p(str(n)):
            permut.append(''.join(i))

        for i in permut:
            if i[0] == '0':
                start_zero = True
            temp_var = int(i)
            while temp_var % 2 == 0:
                temp_var /= 2
            
            if temp_var == 1 and not start_zero:
                return True
                break
            else:
                start_zero = False

        return False
    