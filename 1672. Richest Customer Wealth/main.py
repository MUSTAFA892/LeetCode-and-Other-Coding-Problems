class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            max_wealth = max(customer_wealth,max_wealth)
        return max_wealth