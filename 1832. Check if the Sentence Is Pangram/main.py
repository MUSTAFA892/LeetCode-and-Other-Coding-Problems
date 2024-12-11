class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in sentence:
            if i not in s:
                s.add(i)
        if len(s) == 26:
            return True
        return False