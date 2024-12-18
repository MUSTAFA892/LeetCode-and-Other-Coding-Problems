class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final = []
        for i in range(len(prices)):
            discount = prices[i]
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[i] - prices[j]
                    break
            final.append(discount)
        return final