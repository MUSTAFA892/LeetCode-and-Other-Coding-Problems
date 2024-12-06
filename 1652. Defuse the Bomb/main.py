class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        i , j = 0, 0
        result = [0] * n
        sum_ = 0
        if k == 0:
            return result

        elif k > 0:
            i = 1
            j = k
        
        else:
            i = n - abs(k)
            j = n - 1

        for pointer in range(i , j + 1):
            sum_ += code[pointer]
        
        for k in range(0,n):
            result[k] = sum_

            sum_ -= code[i % n]
            i += 1

            sum_ += code[(j+1)%n]
            j+=1
        
        return result
        
        