class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        set_ = set(banned)
        count = 0
        sum_ = 0
        i = 1

        while i <= n:
            if i not in set_:
                if sum_ + i > maxSum:
                    break
                sum_ += i
                count += 1
            i += 1
        
        return count