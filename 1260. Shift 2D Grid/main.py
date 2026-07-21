class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid

        m, n = len(grid), len(grid[0])

        arr = [[1 for _ in range(n)] for _ in range(m)]
        
        for _ in range(k):
            for i in range(m):
                for j in range(n-1):
                    arr[i][j+1] = grid[i][j]
                if i+1 < m:
                    arr[i+1][0] = grid[i][n-1]
                
            
            arr[0][0] =  grid[m-1][n-1]
            grid = [row[:] for row in arr]

        return arr