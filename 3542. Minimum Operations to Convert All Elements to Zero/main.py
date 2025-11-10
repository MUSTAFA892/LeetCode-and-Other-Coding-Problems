class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        stack = []
        for x in nums:
            if x == 0:

                while stack and stack[-1] > 0:
                    stack.pop()
                continue

            while stack and stack[-1] > x:
                stack.pop()

            if not stack or stack[-1] < x:
                stack.append(x)
                ops += 1

        return ops

"""        ops = 0
        segment = []

        for num in nums + [0]:
            if num == 0:
                if segment:
                    ops += len(Counter(segment))
                    segment = []
            else:
                segment.append(num)
                
        return ops """

"""        freq_nums = nums
        freq_nums.sort()
        freq = Counter(freq_nums)
        ops = 0

        for i , (key,val) in enumerate(freq.items()):
            if i == 0 and key != 0:
                ops += 1
            elif i == 0 and key == 0:
                continue
            else:
                ops += val

        return ops"""