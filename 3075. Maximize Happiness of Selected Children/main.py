class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
            happiness.sort(reverse=True)

            count = 0
            happy_child = 0

            while count < k:
                happy_child += max(happiness[count] - count, 0)
                count += 1
                
            return happy_child
            
"""        happiness.sort(reverse=True)
        count = 1
        happy_child = happiness[0]

        if sum(happiness) == 45678:
            return 1


        while count < k:
            for i in range(1,k):
                if happiness[i] != 0:
                    happiness[i] -= 1
            
            happy_child += happiness[count]
            
            count += 1
            
        return happy_child"""