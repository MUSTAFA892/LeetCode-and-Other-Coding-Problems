class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisor(num):
            arr = [1,num]
        
            for i in range(2,int(math.sqrt(num)) + 1):
                
                if num % i == 0 :
                    arr.append(i)
                    if num // i != i:
                        arr.append(num // i)
                        
                    if len(arr) > 4:
                        break
                    
                    
            if len(arr) == 4:
                return sum(arr)
            else:
                return 0


        sum_ = 0
        for i in nums:
            sum_ += divisor(i)

        return sum_
