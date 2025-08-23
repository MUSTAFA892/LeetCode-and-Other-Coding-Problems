class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = float('inf')
        bottom = 0
        left = float('inf')
        right = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top,i)
                    left = min(left,j)
                    right = max(right,j)
                    bottom = max(bottom,i)

        return ((bottom - top)+1) * ((right - left) + 1 )