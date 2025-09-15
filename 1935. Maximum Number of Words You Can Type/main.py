class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()

        count = len(text)
        flag = False

        for i in text:
            count_txt = Counter(i)
            
            for j in brokenLetters:
                if j in count_txt:
                    flag = True
                
            if flag:
                count -= 1
                flag = False

        return count 