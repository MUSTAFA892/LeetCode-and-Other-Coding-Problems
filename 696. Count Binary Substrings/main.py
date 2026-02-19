class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev_group = 0  
        curr_group = 1  

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_group += 1
            else:

                count += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1

        count += min(prev_group, curr_group)
        return count

"""        count = 0

        for i in range(2,len(s) + 1, 2):
            half = i // 2
            for j in range(0,len(s) - i + 1):
                
                window = s[j:j+i]

                first_half = window[:half]
                second_half = window[half:]

                if first_half[0] != second_half[0]:
                    if first_half.count(first_half[0]) == half:
                        if second_half.count(second_half[0]) == half:
                            count += 1
        return count"""