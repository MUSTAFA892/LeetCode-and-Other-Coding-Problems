class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left , right = 0, len(letters)
        while left  < right :
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid
            else:
                left = mid + 1
            

        return letters[left % len(letters)]
"""        for i in letters:
            if ord(target) < ord(i):
                return i
                break
        
        return letters[0]"""