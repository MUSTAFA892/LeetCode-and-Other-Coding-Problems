class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        def is_prime(n):

            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
            
        for i in range(left,right+1):
            bin_ = bin(i)[2:]
            no_1 = str(bin_).count('1')

            if is_prime(no_1):
                count += 1


        return count 