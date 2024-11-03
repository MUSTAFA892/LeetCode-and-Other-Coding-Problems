class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word = sentence.split()
        for i in range(len(word)):
            if word[i][-1] != word[(i+1)%len(word)][0]:
               return False
        return True