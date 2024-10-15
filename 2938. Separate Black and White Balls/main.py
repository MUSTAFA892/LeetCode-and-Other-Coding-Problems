class Solution:
    def minimumSteps(self, s: str) -> int:
        swap , white = 0 ,0
        for i in s:
            if i == '0':
                swap+=white
            else:
                white += 1
            
        return swap