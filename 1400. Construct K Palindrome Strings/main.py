from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counter = Counter(s)
        odd = 0

        for count in counter.values():
            if count % 2 != 0:
                odd += 1
        if odd > k:
            return False
        else:
            return True