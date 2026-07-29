class Solution:
    def maxProduct(self, n: int) -> int:
        max_pro = 0
        str_n = str(n)

        for i in range(len(str_n)):
            for j in range(i+1,len(str_n)):
                pro = int(str_n[i]) * int(str_n[j])
                max_pro = max(max_pro, pro)

        return max_pro