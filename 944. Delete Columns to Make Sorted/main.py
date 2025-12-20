class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for i in range(len(strs[0])):
            if len(strs[0]) > 1:
                for j in range(1,len(strs)):
                        if ord(strs[j-1][i]) <= ord(strs[j][i]):
                            continue
                        else:
                            count += 1
                            break

            else:
                for i in range(1,len(strs)):
                    if ord(strs[i-1]) <= ord(strs[i]):
                        continue
                    else:
                        count +=1 

        return count 