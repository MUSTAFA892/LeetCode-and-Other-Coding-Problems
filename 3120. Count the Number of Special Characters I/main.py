class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = list(set(word))
        count  = 0
        map_ = {}

        for i in range (len(word)):
            if word[i].lower() not in map_:
                map_[word[i].lower()] = 1                
            else:
                map_[word[i].lower()] += 1

        for i in map_.values():
            if i == 2:
                count += 1
            
        return count