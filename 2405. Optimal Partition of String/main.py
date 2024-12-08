class Solution:
    def partitionString(self, s: str) -> int:
        result = []
        temp = ""
        for char in s:
            if char in temp:
                result.append(temp)
                temp = char
            temp += char
        if temp:
            result.append(temp)
        return len(result)



"""    partition = set()
        count = 1
        for char in s:
            if char in partition:
                count += 1
                partition.clear()
            partition.add(char)

        return count"""