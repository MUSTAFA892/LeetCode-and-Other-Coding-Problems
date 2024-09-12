class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n= (len(matrix)), (len(matrix[0]))
        total = m * n
        left , right = 0 , total - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n

            mid_element = matrix[i][j]
            if target == mid_element:
                return True
            elif target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        return False