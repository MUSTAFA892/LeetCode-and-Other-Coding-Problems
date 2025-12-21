class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        pairs = [0] * (len(strs) - 1)

        for i in range(len(strs[0])):
            temp = pairs[:]
            delete_col = False

            for j in range(1, len(strs)):
                if pairs[j-1] == 0:
                    if ord(strs[j-1][i]) < ord(strs[j][i]):
                        temp[j-1] = 1
                    elif ord(strs[j-1][i]) > ord(strs[j][i]):
                        count += 1
                        delete_col = True
                        break

            if not delete_col:
                pairs = temp

            if all(pairs):
                break

        return count
