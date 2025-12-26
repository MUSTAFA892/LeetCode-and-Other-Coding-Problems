class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_penalty = customers.count('Y')
        min_penalty = total_penalty
        best = 0
                
        for i in range(len(customers)):
            if customers[i] == 'Y':
                total_penalty -= 1
            else:
                total_penalty += 1  

            if total_penalty < min_penalty:
                min_penalty = total_penalty
                best = i + 1

        return best
        
"""        state = [0] * (len(customers))
        min_penalty_idx = []
        min_penalty = float('inf')

        for i in range(len(customers) + 1):
            penalty = 0

            for j in range(len(customers)):
                if j < i: 
                    if customers[j] == 'N':
                        penalty += 1
                else:       
                    if customers[j] == 'Y':
                        penalty += 1

            min_penalty = min(min_penalty, penalty)
            min_penalty_idx.append(penalty)

        return min_penalty_idx.index(min_penalty)
        """