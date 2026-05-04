class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def get_transporse(matrix):
            arr = [[1 for i in range(len(matrix))]for i in range(len(matrix))]
            for k in range(len(matrix)):
                for j in range(len(matrix)):
                    arr[k][j] = matrix[j][k]
            return arr
            
        final = get_transporse(matrix)
        for i in range(len(matrix)):
            matrix[i] = final[i][::-1]
