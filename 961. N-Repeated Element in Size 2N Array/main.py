class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}
        
        for i in nums:
            if i in freq:
                return i

            freq[i] = 1

"""        freq = Counter(nums)

        return freq.most_common()[0][0]
            """