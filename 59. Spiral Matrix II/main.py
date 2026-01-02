class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[1 for _ in range(n)] for _ in range(n)]

        top , bottom = 0, n - 1
        left , right = 0 , n - 1

        arr = []
        val = 1

        while left <= right and top <= bottom:
            

            for i in range(left, right+1):
                grid[top][i] = val
                val += 1
            top += 1

            for j in range(top,bottom+1):
                grid[j][right] = val
                val += 1
            right -= 1
            
            if top <= bottom:
                for k in range(right,left-1,-1):
                    grid[bottom][k] = val
                    val += 1
                bottom -= 1
                
            if left <= right:
                for l in range(bottom,top-1,-1):
                    grid[l][left] = val
                    val += 1
                left += 1

        return grid