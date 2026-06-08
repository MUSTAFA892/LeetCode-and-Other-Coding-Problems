class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost = 0
        pointer = 0 
        cost = sorted(cost, reverse=True)

        while pointer < len(cost):
            if len(cost) > 2:
                for i in range(2):
                    if pointer < len(cost):
                        min_cost += cost[pointer]
                        pointer += 1
            else:
                return sum(cost)

            pointer += 1
            
        return min_cost