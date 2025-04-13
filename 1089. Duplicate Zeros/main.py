class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pointer = 0

        while pointer < len(arr):
            if arr[pointer] == 0:
                arr.insert(pointer + 1 , 0)
                arr.pop()
                pointer += 1
            
            pointer += 1
        

        