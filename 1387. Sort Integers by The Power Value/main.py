class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        map_ = {}
        for i in range(lo,hi+1):
            num = i
            steps = 0

            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3 * num + 1
                steps += 1

            map_[i] = steps

        sort = sorted(map_.items(), key=lambda items : items[1])

        return sort[k-1][0]