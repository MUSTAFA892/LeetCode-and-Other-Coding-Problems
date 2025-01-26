class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = Counter(nums)
        ope = 0

        for i in s.values():
            if i == 1:
                return -1
                break
            
            ope += i // 3
            if i % 3 != 0:
                ope += 1
            
        return ope