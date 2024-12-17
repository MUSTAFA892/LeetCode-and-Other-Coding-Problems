class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char = sorted(s, reverse=True)
        result = []
        freq = 1
        pointer = 0

        for i in range(len(char)):
            if result and result[-1] == char[i]:
                if freq < repeatLimit:
                    result.append(char[i])
                    freq += 1
                else:
                    pointer = max(pointer, i+1)
                    while pointer < len(char) and char[pointer] == char[i]:
                        pointer += 1
                    if pointer < len(char):
                        result.append(char[pointer])
                        char[i], char[pointer] = char[pointer] , char[i]
                        freq = 1
                    else:
                        break
            else:
                result.append(char[i])
                freq = 1
        return ''.join(result)