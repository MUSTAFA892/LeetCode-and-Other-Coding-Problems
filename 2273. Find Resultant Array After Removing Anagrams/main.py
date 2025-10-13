class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        check = [words[0]]
        og = [''.join(sorted(words[0]))]

        for i in range(1,len(words)):
            if ''.join(sorted(words[i])) == og[-1]:
                og.append(''.join(sorted(words[i])))
            
            else:
                og.append(''.join(sorted(words[i])))
                check.append(words[i])
        
        return check 