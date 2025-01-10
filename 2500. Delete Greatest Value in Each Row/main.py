class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = []

        while len(grid[0]) > 0 :
            max_value = []

            for row in grid:
                max_ = max(row)
                max_value.append(max_)
                row.remove(max_)
            
            ans.append(max(max_value))
        

        return sum(ans)