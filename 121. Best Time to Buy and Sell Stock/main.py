class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0 , 1 
        max_point = 0
        while right < (len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_point = max(profit,max_point)
            else:
                left = right
            right+=1
        return max_point