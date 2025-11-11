class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            new = {}
            
            for (PrevZeros , PrevOnes) , val in dp.items():
                NewZeros , NewOnes = PrevZeros + zeros , PrevOnes + ones
                
                if NewZeros <= m and NewOnes <= n:
                    if (NewZeros,NewOnes) not in dp or dp[(NewZeros,NewOnes)] < val + 1:
                        new[(NewZeros,NewOnes)] = val + 1
                        
                
            dp.update(new)
        
        return max(dp.values())

"""        
        max_size = 0

        for r in range(1, len(strs) + 1):             
            for subset in itertools.combinations(strs, r): 
                zeros = sum(s.count('0') for s in subset)
                ones = sum(s.count('1') for s in subset)

                if zeros <= m and ones <= n:
                    max_size = max(max_size, len(subset))

        return max_size"""