class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Convert magazine to a list of characters
        lst_magazine = list(magazine)
        
        # Iterate through each character in ransomNote
        for char in ransomNote:
            if char in lst_magazine:
                lst_magazine.remove(char)  # Remove one occurrence of the char from magazine
            else:
                return False  # If char not found in magazine, return False
        
        # If all characters were found and removed, return True
        return True