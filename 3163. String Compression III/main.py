class Solution:
    def compressedString(self, word: str) -> str:
        word+="["
        comp=""
        i=0
        while i < len(word)-1:
            temp = word[i]
            count=1
            while count<9 and temp == word[i+1]:
                i+=1
                count+=1
            comp+=str(count)+temp
            i+=1
                
        return comp
