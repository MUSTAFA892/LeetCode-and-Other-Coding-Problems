class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []

        for i in range(rowIndex+1):
            temp_arr = [1] * (i+1)
            
            for j in range(1,i):
                print('j',j)
                
                temp_arr[j] = arr[i-1][j-1] + arr[i-1][j]

            
            arr.append(temp_arr)
        
        return arr[-1]