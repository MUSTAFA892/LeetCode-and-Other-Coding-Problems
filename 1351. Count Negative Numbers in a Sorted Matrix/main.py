class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        len_row , len_col = len(grid) , len(grid[0])
        row , col = 0, len_col - 1
        count = 0

        while row < len_row and col >= 0:
            if grid[row][col] < 0:
                count += len_row - row
                col -= 1
            else:
                row += 1

        return count
"""        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
                
        return count"""