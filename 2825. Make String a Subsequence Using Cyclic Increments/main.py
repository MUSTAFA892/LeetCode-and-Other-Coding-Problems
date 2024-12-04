class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        i, j = 0, 0
        
        while i < n and j < m:
            if str1[i] == str2[j] or str1[i] == 'z' and str2[j] == 'a' or ord(str1[i]) + 1 == ord(str2[j]):
                i += 1
                j += 1
            else:
                i += 1
        

        return j == m