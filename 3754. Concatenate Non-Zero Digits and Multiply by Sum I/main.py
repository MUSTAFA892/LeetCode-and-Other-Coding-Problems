class Solution:
    def sumAndMultiply(self, n: int) -> int:
        count = 0
        dum_n = ''

        for i in str(n):
            if int(i) > 0:
                count += int(i)
                dum_n += i

        if count > 0:
            return int(dum_n) * count

        return 0