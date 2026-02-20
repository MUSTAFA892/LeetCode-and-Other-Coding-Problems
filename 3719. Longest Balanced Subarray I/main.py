class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            even_set = set()
            odd_set = set()

            for j in range(i, n):
                num = nums[j]

                if num % 2 == 0:
                    even_set.add(num)
                else:
                    odd_set.add(num)

                if len(even_set) == len(odd_set):
                    max_len = max(max_len, j - i + 1)

        return max_len