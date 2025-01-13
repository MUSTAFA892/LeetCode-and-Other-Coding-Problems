from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        a = Counter(s)
        counter = 0
        for char , count in a.items():
            if count % 2 == 0:
                counter += 2
            else:
                counter += 1 
        return counter

        
"""        a = Counter(s)
        counter = 0
        while True:
            modified = False
            for char, count in list(a.items()):
                if count >= 3:
                    a[char] -= 2
                    modified = True
            if not modified:
                break
        for count in a.values():
            counter += count
        return counter"""
     