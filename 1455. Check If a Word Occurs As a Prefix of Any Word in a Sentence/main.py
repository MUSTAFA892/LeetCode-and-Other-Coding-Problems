class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split = sentence.split()
        for i in split:
            if searchWord in i[:len(searchWord)]:
                return split.index(i) + 1
                break
        return -1