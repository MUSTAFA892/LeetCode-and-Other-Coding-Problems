from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        
        counter_words2 = Counter()
        for word in words2:
            counter_words2 |= Counter(word)

        for word in words1:
            word_count = Counter(word)

            found = True
            for char , count in counter_words2.items():
                if word_count[char] < count:
                    found = False
                    break

            if found:
                result.append(word)

        return result 
