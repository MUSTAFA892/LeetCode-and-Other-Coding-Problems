class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []

        for i in nums:
            a = list(str(i))
            for j in a:
                arr.append(int(j))
                
        return arr