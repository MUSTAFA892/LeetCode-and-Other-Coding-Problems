class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in diagonals:
                   diagonals[i+j] = [] 
                diagonals[i+j].append(mat[i][j])

        ans = []
        for key ,val in diagonals.items():
            if key % 2 == 0:
                ans.extend(val[::-1])
            else:
                ans.extend(val)

        return ans

