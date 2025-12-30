class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0

        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                
                nums = []
                for i in range(r, r + 3):
                    for j in range(c,c+3):
                        nums.append(grid[i][j])
                        
                if sorted(nums) != [1,2,3,4,5,6,7,8,9]:
                    continue

                row1 = grid[r][c]   + grid[r][c+1]   + grid[r][c+2]
                row2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
                row3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]

                col1 = grid[r][c]   + grid[r+1][c]   + grid[r+2][c]
                col2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                col3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]

                d1 = grid[r][c]     + grid[r+1][c+1] + grid[r+2][c+2]
                d2 = grid[r][c+2]   + grid[r+1][c+1] + grid[r+2][c]

                if (row1 == row2 == row3 ==
                    col1 == col2 == col3 ==
                    d1 == d2 == 15):
                    count += 1
                
        return count