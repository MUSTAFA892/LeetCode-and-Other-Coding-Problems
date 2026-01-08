class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        total = rows * cols
        r, c = rStart, cStart
        
        if 0 <= r < rows and 0 <= c < cols:
            ans.append([r, c])
        
        layer = 1
        while len(ans) < total:
            for _ in range(layer):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            for _ in range(layer):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            layer += 1
            
            for _ in range(layer):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            for _ in range(layer):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            
            layer += 1
        
        return ans