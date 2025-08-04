class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_fruits = 0
        steps = 0

        left = 0
        current_fruits = 0
        for right  in range(n):
            current_fruits += fruits[right][1]
            while left <= right:

                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                if startPos <= left_pos:
                    steps = right_pos - startPos
                elif startPos >= right_pos:
                    steps = startPos - left_pos
                else:
                    steps = min(abs(startPos - left_pos),abs(startPos - right_pos)) + (right_pos - left_pos)

                if steps <= k:
                    break
                else:
                    current_fruits -= fruits[left][1]
                    left += 1

            max_fruits = max(max_fruits,current_fruits)

        return max_fruits