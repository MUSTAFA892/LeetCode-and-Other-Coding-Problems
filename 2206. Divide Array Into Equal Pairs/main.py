class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        flag = False
        freq = Counter(nums)

        for count in freq.values():
            if count % 2 == 0:
                flag = True
            else:
                flag = False
                break

        return flag
            