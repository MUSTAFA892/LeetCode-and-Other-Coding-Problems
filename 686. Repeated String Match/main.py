class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        check_str = ""
        count = 0

        while len(check_str) < len(b):
            check_str += a
            count += 1
        if b in check_str:
            return count

        check_str += a
        count += 1

        if b in check_str:
            return count
        
        return -1
        