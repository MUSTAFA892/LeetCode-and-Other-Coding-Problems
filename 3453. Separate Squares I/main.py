class Solution:
    def separateSquares(self, squares):
        total_area = 0
        for x, y, l in squares:
            total_area += l * l
        
        target = total_area / 2

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):   
            mid = (low + high) / 2
            below = 0

            for x, y, l in squares:
                bottom = y
                top = y + l

                if mid <= bottom:
                    continue
                elif mid >= top:
                    below += l * l
                else:
                    below += l * (mid - bottom)

            if below < target:
                low = mid
            else:
                high = mid

        return low
