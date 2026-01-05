class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        s = []

        while a > 0 or b > 0:

            if a > b:
                take = min(2,a)
                s.extend('a' * take)
                a -= take

                if b > 0:
                    s.append('b')
                    b -= 1
            
            elif a < b:
                take = min(2,b)
                s.extend('b' * take)
                b -= take

                if a > 0:
                    s.append('a')
                    a -= 1

            else:
                s.append('a')
                a -= 1
                s.append('b')
                b -= 1
            
        return ''.join(s)