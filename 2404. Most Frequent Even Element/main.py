class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [i for i in nums if i %  2 == 0]

        max_freq = 0
        max_freq_value = -1
        even_nums.sort()
        freq = Counter(even_nums)
        if freq:
            for value , count in freq.items():
                if count > max_freq:
                    max_freq = count
                    max_freq_value = value
        else:
            return -1
        return max_freq_value