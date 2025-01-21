class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefixRow1 , prefixRow2 = grid[0] , grid[1]

        for i in range(1,len(grid[0])):
            prefixRow1[i] += prefixRow1[i-1]
            prefixRow2[i] += prefixRow2[i-1]
        
        res = float('inf') 

        for i in range(len(grid[0])):
            top = prefixRow1[-1] - prefixRow1[i]
            bottom = prefixRow2[i-1] if i > 0 else 0
            second_robot = max(top, bottom)
            res = min(res,second_robot)

        
        return res



class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum, bottomSum = sum(grid[0]), 0

        for i in range(len(grid[0]) - 1):
            topSum -= grid[0][i]
            bottomSum += grid[1][i]
            if (bottomSum >= topSum):
                bottomSum -= grid[1][i]
                if topSum > bottomSum:
                    return topSum
                return bottomSum

        # if we never went to the bottom
        return bottomSum