class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count = 0
        capacity.sort(reverse=True)
        apple_filled = 0

        for i in capacity:
            if apple_filled < sum(apple):
                apple_filled += i
                count += 1
            else:
                break

        return count