class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        pos = []
        neg = [] 
        
        for i in nums:
            if i == 0:
                return 0 
            elif i < 0:
                neg.append(i)
            else:
                pos.append(i)
            

        if not pos:
            return sorted(neg)[-1]

        if not neg:
            return sorted(pos)[0]
        
        if abs(sorted(neg)[-1]) < sorted(pos)[0]:
            return sorted(neg)[-1]
        else:
            return sorted(pos)[0]