class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ = 0
        max_left = values[0]

        for i in range(1,len(values)):
            max_ = max(max_, max_left + values[i] - i)
            max_left = max(max_left, values[i] + i)

        return max_