class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        count = 0
        week_start = 1
        week_end = 0
        deposit = week_start

        while day < n:
            count += deposit
            day += 1
            week_end += 1
            deposit += 1

            if week_end == 7:
                week_start += 1
                deposit = week_start
                week_end = 0

        return count 