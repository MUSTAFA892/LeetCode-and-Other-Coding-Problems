class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []

        for i in range(left, right+1):
            num = str(i)
            flag = True
            for j in num:
                if int(j) != 0:
                    if int(num) % int(j) != 0:
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag:
                arr.append(i)

        return arr   
