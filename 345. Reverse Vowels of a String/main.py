class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        result = []
        index = []
        vowels = ['A','a','E','e','I','i','O','o','U','u']

        for i in range(len(s)):
            if s[i] in vowels:
                result.append(s[i])
                index.append(i)
        result.reverse()

        for idx , vowel in zip(index,result):
            s[idx] = vowel
        
        return "".join(s)