from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for k , v in freq.items():
            if v >= 2:
                ans.append(k)
        
        return ans