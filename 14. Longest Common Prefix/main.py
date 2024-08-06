class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)

        first = strs[0]
        Last = strs[-1]

        for i in range (min((len(first)),(len(Last)))):
            if first[i] == Last[i]:
                ans+=first[i]
            else:
                return ans
                break
        return ans
