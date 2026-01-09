from itertools import combinations
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n, m = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i-1] * nums2[j-1]
                
                dp[i][j] = max(
                    prod,                      
                    dp[i-1][j-1] + prod,        
                    dp[i-1][j],                 
                    dp[i][j-1]                  
                )
        return dp[n][m]

"""        arr1 = []
        arr2 = []

        max_product = float('-inf')

        max_len = min(len(nums1), len(nums2))

        for r in range(1, max_len + 1):
            arr1.extend(combinations(nums1, r))
            arr2.extend(combinations(nums2, r))

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if len(arr1[i]) == len(arr2[j]):
                    dot = 0
                    for k in range(len(arr1[i])):
                        dot += arr1[i][k] * arr2[j][k]
                    max_product = max(max_product, dot)

        return max_product
"""