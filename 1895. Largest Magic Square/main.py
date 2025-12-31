class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid) , len(grid[0])

        k = min(m,n)
        count = 1

        while k != 1:

            for r in range(m-k+1):
                for c in range(n-k+1):
                    
                    ok = True
                    target = sum(grid[r][c:c+k])
                    
                    for i in range(k):
                        row = 0
                        for j in range(k):
                            row += grid[r + i][c + j]
                            
                        if row != target:
                            ok = False
                            break
                
                    if ok:              
                        for i in range(k):
                            col = 0
                            for j in range(k):  
                                col += grid[r +j][c + i]
                                
                            if col != target:
                                ok =False
                                break

                    if ok:        
                        d1 = 0
                        d2 = 0
                        for i in range(k):
                            d1 += grid[r + i][c + i]
                            d2 += grid[r + i][c + (k-1) - i]
                            
                        if d1 != target or d2 != target:
                            ok = False               
                        
                    if ok:
                        return k           

            k -= 1

        return 1
                