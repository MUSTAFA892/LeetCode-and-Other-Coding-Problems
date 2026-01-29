class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            arr = matrix[i]
            l , r = 0 , len(arr) - 1
            flag = False
            
            while l <= r:
                mid = (l+r) // 2
                if target == arr[mid]:
                    flag = True
                    break
                    
                elif target < arr[mid]:
                    r = mid -1
                    
                else:
                    l = mid + 1
                    
            if flag:
                return True
                break
        
        return False