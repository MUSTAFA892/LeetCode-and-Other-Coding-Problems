class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [[0,0]]
        final_arr = ["".join(["#" for _ in range(n)]) for _ in range(m)]
        level = 0

        stop = False
        change = 0
        while not stop:
            
            if change == 0:
                if arr[-1] != [m-1,n-1]:
                    val = [arr[-1][0],arr[-1][1]+1]
                    if val[1] < n:
                        arr.append(val)
                        change = 1
                    else:
                        val = [arr[-1][0]+1,arr[-1][1]]
                        arr.append(val)
                        change = 0
                else:
                    stop = True
                    
            else :
                if arr[-1] != [m-1,n-1]:
                    val = [arr[-1][0]+1,arr[-1][1]]
                    if val[0] < m:
                        arr.append(val)
                        change = 0
                    else:
                        val = [arr[-1][0],arr[-1][1]+1]
                        arr.append(val)
                        change = 1
                else:
                    stop = True

        for i in arr:
            row = i[0]
            col = i[1]

            final_arr[row] = final_arr[row][:col] + "." + final_arr[row][col+1:]
        

        return final_arr