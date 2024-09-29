class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_splitting = s.split()
        return len(word_splitting[-1])