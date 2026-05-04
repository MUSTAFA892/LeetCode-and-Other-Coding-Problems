class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def get_transporse(mat):
            arr = [[1 for i in range(len(mat))]for i in range(len(mat))]
            for k in range(len(mat)):
                for j in range(len(mat)):
                    arr[k][j] = mat[j][k]
            return arr

        for _ in range(4):  
            final = get_transporse(mat)
            for i in range(len(mat)):
                mat[i] = final[i][::-1]

            flag = True
            for j in range(len(mat)):
                for k in range(len(mat)):
                    if mat[k][j] != target[k][j]:
                        flag = False
                        break
                if not flag:
                    break
            
            if flag:
                return True

        return False