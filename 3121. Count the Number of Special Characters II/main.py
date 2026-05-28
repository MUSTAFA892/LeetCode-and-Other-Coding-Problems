class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = list(word)
        count = 0
        running = []
        map_ = {}

        for i in range(len(word)):
            
            if word[i].lower() not in map_:
                if word[i].isupper():
                    map_[word[i].lower()] = -1
                else:
                    map_[word[i].lower()] = 1
                running.append(word[i])

            else:

                if word[i].islower() and map_[word[i].lower()] == 2:
                    map_[word[i].lower()] = -1 
                
                elif word[i].isupper() and map_[word[i].lower()] == 1:
                    map_[word[i].lower()] = 2 
                
                running.append(word[i])

        for i in map_.values():
            if i == 2:
                count += 1
            
        return count