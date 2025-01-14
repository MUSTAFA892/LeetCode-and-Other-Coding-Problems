class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []

        for i in range(len(A)):

            count = 0

            for num in A[:i+1]:
                if num in B[:i+1]:
                    count += 1
            ans.append(count)

        return ans