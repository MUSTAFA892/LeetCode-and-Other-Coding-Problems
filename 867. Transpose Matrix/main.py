class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range (len(matrix[0])):
            arr = []
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            ans.append(arr)

        return ans