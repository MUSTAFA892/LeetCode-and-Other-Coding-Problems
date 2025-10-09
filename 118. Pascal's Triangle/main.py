class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []

        for i in range(numRows):
            temp_arr = [1] * (i+1)
            
            for j in range(1,i):
                
                temp_arr[j] = arr[i-1][j-1] + arr[i-1][j]

            
            arr.append(temp_arr)
        
        return arr