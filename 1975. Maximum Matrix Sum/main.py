class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_val = []
        sum_ = 0
        min_val = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    neg_val.append(matrix[i][j])
                    matrix[i][j] = -(matrix[i][j])
                    
                sum_ += matrix[i][j]
                min_val = min(min_val,matrix[i][j])
                
        if len(neg_val) % 2 != 0:
            return sum_ - (2 * min_val)
        else:
            return sum_