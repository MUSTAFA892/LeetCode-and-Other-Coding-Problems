import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        count = 0
        while count < k:
            max_ = max(gifts)
            gifts.remove(max_)
            gifts.append(math.floor(math.sqrt(max_)))
            count += 1
        
        return sum(gifts)