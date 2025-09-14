class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        arr = []

        filter1_map = set(wordlist)
        filter2_map = {}
        filter3_map = {}

        def mask_word(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        for i in range(len(wordlist)):
            lower = wordlist[i].lower()
            if lower not in filter2_map:
                filter2_map[lower] = wordlist[i]
                
        for i in range(len(wordlist)):
            masked = mask_word(wordlist[i].lower())
            if masked not in filter3_map:
                filter3_map[masked] = wordlist[i]

        for i in queries:
            if i in filter1_map:
                arr.append(i)
                
            elif i.lower() in filter2_map:
                arr.append(filter2_map[i.lower()])
                
            elif mask_word(i.lower()) in filter3_map:
                arr.append(filter3_map[mask_word(i.lower())])
            
            else:
                arr.append("")
            
        return arr



"""class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        arr = []

        def filter_2(val):
            for i in range(len(wordlist)):
                if val.lower() == wordlist[i].lower():
                    return wordlist[i]
                    

        def mask_word(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)


        def filter_3(val):
            for i in range(len(wordlist)):
                if len(val) == len(wordlist[i]):
                    if mask_word(val.lower()) == mask_word(wordlist[i].lower()):
                        return wordlist[i]


        for i in queries:
            if i in wordlist:
                arr.append(i)
                
            elif filter_2(i):
                arr.append(filter_2(i))
                
            elif filter_3(i):
                arr.append(filter_3(i))
            
            else:
                arr.append("")

        return arr"""