class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 0
        consonants = 0
        special_char = False

        if len(word) < 3:
            return False

        for i in word:
            if not i.isalnum():
                special_char = True
                break
            if i.isalpha():
                if i.lower() in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1
        if vowels > 0 and consonants > 0 and not special_char:
            return True
        else:
            return False