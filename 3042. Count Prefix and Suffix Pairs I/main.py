class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                    if words[j][:len(words[i])] == words[i] and words[j][-len(words[i]):] == words[i]:
                        count += 1
        return count