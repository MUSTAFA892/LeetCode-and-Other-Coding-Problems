class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        top , bottom = 0, len(grid) - 1
        left , right = 0 , len(grid[0]) - 1

        arr = []

        if len(grid) <= 1:
            return grid[0]

        while left <= right and top <= bottom:

            for i in range(left, right+1):
                arr.append(grid[top][i])
            top += 1

            for j in range(top,bottom+1):
                arr.append(grid[j][right])
            right -= 1

            if top <= bottom:
                for k in range(right,left-1,-1):
                    arr.append(grid[bottom][k])
                bottom -= 1
            
            if left <= right:
                for l in range(bottom,top-1,-1):
                    arr.append(grid[l][left])
                left += 1

        return arr