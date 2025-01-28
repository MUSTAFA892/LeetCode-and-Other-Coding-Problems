class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(num)-1,-1,-1):
            k += num[i]
            result.append(k%10)
            k //= 10

        while k > 0:
            result.append(k%10)
            k //= 10
        return result[::-1] 